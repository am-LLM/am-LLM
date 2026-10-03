#!/usr/bin/env python3
"""
CISSP Quantitative Risk Assessment & Cost-Benefit Analysis Solver
Computes SLE, ALE, and Cost-Benefit of Security Safeguards per NIST SP 800-30 / CISSP Domain 1.
"""

def calculate_risk(asset_value: float, exposure_factor: float, aro: float, safeguard_annual_cost: float, mitigated_aro: float):
    sle = asset_value * exposure_factor
    ale_prior = sle * aro
    ale_post = sle * mitigated_aro
    annual_savings = ale_prior - ale_post
    cba = annual_savings - safeguard_annual_cost
    return {
        "SLE": sle,
        "ALE_Prior": ale_prior,
        "ALE_Post": ale_post,
        "Annual_Savings": annual_savings,
        "Safeguard_Cost": safeguard_annual_cost,
        "Net_Benefit": cba,
        "Viable": cba > 0
    }

if __name__ == "__main__":
    report = calculate_risk(
        asset_value=5000000.0,
        exposure_factor=0.30,
        aro=0.5,
        safeguard_annual_cost=80000.0,
        mitigated_aro=0.05
    )
    print("=== CISSP Quantitative Risk Assessment Report ===")
    for k, v in report.items():
        print(f"  {k}: {v:,.2f}" if isinstance(v, float) else f"  {k}: {v}")
