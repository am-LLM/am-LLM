#!/usr/bin/env python3
"""
OSCP Lab Tool: Kerberos SPN & UAC Flag Offline Audit Simulator
Demonstrates detection of accounts vulnerable to AS-REP Roasting & Kerberoasting.
"""

import struct

class KerberosTicketInspector:
    def __init__(self, domain: str):
        self.domain = domain.upper()
        self.user_database = []

    def register_account(self, username: str, spn: str = None, uac_dont_req_preauth: bool = False):
        self.user_database.append({
            "username": username,
            "spn": spn,
            "dont_req_preauth": uac_dont_req_preauth
        })

    def audit_vulnerabilities(self):
        vulnerabilities = []
        for acct in self.user_database:
            if acct["dont_req_preauth"]:
                vulnerabilities.append({
                    "target": f"{self.domain}\\{acct['username']}",
                    "attack_type": "AS-REP Roasting (Hashcat Mode 18200)",
                    "remediation": "Enable Kerberos Pre-Authentication in UserAccountControl"
                })
            if acct["spn"]:
                vulnerabilities.append({
                    "target": f"{self.domain}\\{acct['username']} ({acct['spn']})",
                    "attack_type": "Kerberoasting (Hashcat Mode 13100)",
                    "remediation": "Migrate service account to Group Managed Service Account (gMSA)"
                })
        return vulnerabilities

if __name__ == "__main__":
    inspector = KerberosTicketInspector("CORP.LOCAL")
    inspector.register_account("svc_backup", spn="MSSQLSvc/db01.corp.local:1433", uac_dont_req_preauth=False)
    inspector.register_account("legacy_user", spn=None, uac_dont_req_preauth=True)
    inspector.register_account("admin_user", spn=None, uac_dont_req_preauth=False)
    
    findings = inspector.audit_vulnerabilities()
    print(f"[*] Kerberos Attack Surface Audit for {inspector.domain}:")
    for f in findings:
        print(f"  [!] {f['target']} -> {f['attack_type']}")
        print(f"      Remediation: {f['remediation']}")
