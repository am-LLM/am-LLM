#!/usr/bin/env python3
"""
CFI FMVA Module: DCF Enterprise Valuation & SaaS LTV/CAC Solver
"""

def calculate_dcf(cash_flows: list, wacc: float, terminal_growth: float) -> dict:
    discounted_cf = [cf / ((1 + wacc) ** (i + 1)) for i, cf in enumerate(cash_flows)]
    last_cf = cash_flows[-1]
    terminal_val = (last_cf * (1 + terminal_growth)) / (wacc - terminal_growth)
    discounted_tv = terminal_val / ((1 + wacc) ** len(cash_flows))
    enterprise_value = sum(discounted_cf) + discounted_tv
    return {
        "PV_Cash_Flows": sum(discounted_cf),
        "PV_Terminal_Value": discounted_tv,
        "Enterprise_Value": enterprise_value
    }

if __name__ == "__main__":
    projections = [1200000, 1600000, 2100000, 2800000, 3600000]
    val = calculate_dcf(projections, wacc=0.095, terminal_growth=0.025)
    print("=== CFI FMVA Enterprise Valuation Report ===")
    for k, v in val.items():
        print(f"  {k}: ${v:,.2f}")
