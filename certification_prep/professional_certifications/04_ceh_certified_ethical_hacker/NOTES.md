# CEH Ethical Hacking & Reconnaissance Engineering Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: EC-Council CEH v12. Nmap Port Scanning Mechanics, Packet Crafting, and Wireless Security.

---

## 1. Nmap TCP Handshake & Firewall Evasion Scans

### 1.1 TCP SYN Stealth Scan (`-sS`)
* Sends TCP SYN $ightarrow$ Receives `SYN/ACK` (Open) $ightarrow$ Client sends `RST` to terminate without completing handshake.

### 1.2 TCP FIN, NULL & Xmas Scans (RFC 793 Behavior)
* **NULL Scan (`-sN`)**: No flags set.
* **FIN Scan (`-sF`)**: Only FIN bit set.
* **Xmas Scan (`-sX`)**: FIN, PSH, and URG flags set (lights up like a Christmas tree).
* *Rule*: Open/Filtered port drops the packet without response; Closed port responds with `RST/ACK`.

```bash
# Optimized Nmap Fast Network Sweep
nmap -sS -p 1-65535 -T4 --min-rate 1000 -n -Pn 192.168.1.0/24 -oA network_scan_full
```
