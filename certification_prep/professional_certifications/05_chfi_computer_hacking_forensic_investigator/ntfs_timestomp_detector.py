#!/usr/bin/env python3
"""
CHFI Digital Forensics Tool: NTFS $STANDARD_INFORMATION vs $FILE_NAME Timestomp Detector
Detects anti-forensic timestamp tampering in Windows file systems.
"""

import datetime

class MFTRecord:
    def __init__(self, filename: str, si_modified: str, fn_modified: str):
        self.filename = filename
        self.si_modified = datetime.datetime.fromisoformat(si_modified)
        self.fn_modified = datetime.datetime.fromisoformat(fn_modified)

    def is_timestomped(self) -> bool:
        # If $STANDARD_INFORMATION modified is older than $FILE_NAME modified, tampering occurred
        return self.si_modified < self.fn_modified

if __name__ == "__main__":
    records = [
        MFTRecord("svchost_legit.exe", "2023-01-15T10:00:00", "2023-01-15T10:00:00"),
        MFTRecord("payload_evil.exe", "2019-05-01T04:20:00", "2026-10-02T14:30:00")
    ]
    
    print("[*] Forensic MFT Timestomp Analysis:")
    for r in records:
        status = "MALICIOUS (Timestomped detected)" if r.is_timestomped() else "CLEAN"
        print(f"  File: {r.filename:<20} | Status: {status}")
