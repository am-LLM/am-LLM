#!/usr/bin/env python3
"""
NEBOSH & OSHA Industrial Safety: TRIR Incident Rate & 5x5 Risk Matrix Calculator
Computes Total Recordable Incident Rate and evaluates residual hazard risks.
"""

def compute_trir(total_recordable_cases: int, total_hours_worked: float) -> float:
    if total_hours_worked <= 0:
        return 0.0
    return (total_recordable_cases * 200000.0) / total_hours_worked

def evaluate_risk_level(severity: int, likelihood: int) -> str:
    # 5x5 Risk Matrix (Severity 1-5, Likelihood 1-5)
    score = severity * likelihood
    if score >= 15:
        return "CRITICAL (Immediate Work Stoppage)"
    elif score >= 8:
        return "MEDIUM (Engineering & Admin Controls Required)"
    else:
        return "LOW (Acceptable Risk with Standard PPE)"

if __name__ == "__main__":
    hours = 1250000.0
    injuries = 2
    trir = compute_trir(injuries, hours)
    print(f"[*] Facility Occupational Safety Metrics:")
    print(f"  Total Hours Worked: {hours:,.0f} hrs")
    print(f"  Total Recordable Cases: {injuries}")
    print(f"  Facility TRIR: {trir:.2f} (Industry benchmark: < 3.0)")
    print(f"  Confined Space Entry Risk (Sev=4, Lik=3): {evaluate_risk_level(4, 3)}")
