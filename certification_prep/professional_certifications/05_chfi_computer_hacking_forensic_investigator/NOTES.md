# CHFI Digital Forensics & Evidence Preservation Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: EC-Council CHFI v10. Volatility Memory Analysis, File System Carving, Master File Table (MFT) Timelines, and Chain of Custody.

---

## 1. Volatile Memory Forensics & Process Carving (Volatility 3)

```bash
# List active and unlinked hidden processes (DKOM Rootkit detection)
vol -f memory.raw windows.pslist
vol -f memory.raw windows.psscan

# Detect process injection (reflective DLL, hollowed process)
vol -f memory.raw windows.malfind

# Extract network connections at memory acquisition time
vol -f memory.raw windows.netscan
```

---

## 2. NTFS File System Timestamps ($STANDARD_INFORMATION vs $FILE_NAME)

* **$STANDARD_INFORMATION ($SI)**: Easily modified by userland APIs (vulnerable to Timestomping).
* **$FILE_NAME ($FN)**: Only updated by the Windows NT kernel on file rename/move (authoritative baseline for timeline reconstruction).
* *Rule*: If $\$SI < \$FN$, the file has been timestomped by malware.
