# Computer Hacking Forensic Investigator (CHFI v10) — Evidence & Investigation Manual

## 1. Digital Forensics Process & Legal Chain of Custody

```
              EVIDENCE HANDLING PIPELINE (ISO/IEC 27037)
 ┌───────────────┐      ┌───────────────┐      ┌───────────────┐      ┌───────────────┐
 │ 1. Seizure &  │ ───> │ 2. Bit-Stream │ ───> │ 3. Cryptogr.  │ ───> │ 4. Forensic   │
 │   Isolation   │      │    Acquisition│      │    Hashing    │      │    Analysis   │
 └───────────────┘      └───────────────┘      └───────────────┘      └───────────────┘
```

### Forensic Imaging Standards:
* Hardware write-blocker must be physically attached before disk connection.
* Always generate raw bit-stream (`dd`, `E01`, `AFF4`) copies.
* Compute MD5 and SHA-256 hashes immediately post-acquisition and verify against working copy hash before analysis:
  ```bash
  ewfcreate -d /dev/sdb -t evidence_disk -f encase6 -S 2G
  sha256sum /dev/sdb evidence_disk.E01
  ```

---

## 2. Windows NTFS File System Forensics

### Master File Table ($MFT) Record Structure (1024 Bytes)
Each $MFT record contains attributes defining metadata and file content:
* `0x10` (`$STANDARD_INFORMATION` - `$SI`): Stores basic file timestamps (MACB: Modified, Accessed, MFT Created, Born/Created), security ID, attributes.
  * *Vulnerability*: Editable by userland APIs (`SetFileTime`).
* `0x30` (`$FILE_NAME` - `$FN`): Stores file name, parent folder record, and MACB timestamps.
  * *Integrity*: Updated **only by the Windows NTFS kernel driver**.
* **Timestomping Heuristic Rule**:
  $$\text{If } \$SI.\text{Created} < \$FN.\text{Created} \implies \text{Timestomping Detected (Anti-Forensics)}$$

---

## 3. Volatility 3 Memory Forensics Framework

```bash
# Process list & hidden process identification (DKOM unlinking)
vol -f memory.raw windows.pslist
vol -f memory.raw windows.psscan
vol -f memory.raw windows.pstree

# Network connection extraction
vol -f memory.raw windows.netscan

# Injected code and malicious DLL detection (VAD tree analysis)
vol -f memory.raw windows.malfind --dump

# Registry hive dump (SAM and SYSTEM for local credential extraction)
vol -f memory.raw windows.registry.hivelist
vol -f memory.raw windows.hashdump
```
