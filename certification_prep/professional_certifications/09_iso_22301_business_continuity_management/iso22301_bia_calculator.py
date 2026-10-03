#!/usr/bin/env python3
"""
ISO 22301 BIA Engine: RTO, RPO & Maximum Tolerable Disruption Validation
Verifies disaster recovery alignment with ISO 22301 compliance parameters.
"""

def audit_bcm_compliance(critical_process: str, mtpd_hours: float, current_rto_hours: float, current_rpo_hours: float, max_allowed_data_loss_hours: float):
    compliant_rto = current_rto_hours < mtpd_hours
    compliant_rpo = current_rpo_hours <= max_allowed_data_loss_hours
    return {
        "Process": critical_process,
        "MTPD_Hours": mtpd_hours,
        "RTO_Hours": current_rto_hours,
        "RPO_Hours": current_rpo_hours,
        "RTO_Compliant": compliant_rto,
        "RPO_Compliant": compliant_rpo,
        "ISO_22301_Certified_Ready": compliant_rto and compliant_rpo
    }

if __name__ == "__main__":
    report = audit_bcm_compliance("Core Payment Gateway", mtpd_hours=4.0, current_rto_hours=1.5, current_rpo_hours=0.25, max_allowed_data_loss_hours=0.5)
    print("[*] ISO 22301 Business Impact Analysis (BIA) Audit:")
    for k, v in report.items():
        print(f"  {k}: {v}")
