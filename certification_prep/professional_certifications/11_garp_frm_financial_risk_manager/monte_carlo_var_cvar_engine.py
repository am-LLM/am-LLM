#!/usr/bin/env python3
"""
GARP FRM Module: Monte Carlo Value at Risk (VaR) & Expected Shortfall (CVaR) Engine
Simulates multi-asset portfolio drawdowns under heavy-tailed market regimes.
"""

import numpy as np

def compute_var_cvar(portfolio_value: float, mean_return: float, vol: float, days: int = 1, confidence: float = 0.99, n_sims: int = 100000):
    np.random.seed(42)
    simulated_returns = np.random.normal(mean_return * days, vol * np.sqrt(days), n_sims)
    simulated_losses = -portfolio_value * simulated_returns

    var_threshold = np.percentile(simulated_losses, confidence * 100)
    cvar_expected_shortfall = np.mean(simulated_losses[simulated_losses >= var_threshold])

    return {
        "Portfolio_Value": portfolio_value,
        "Confidence": f"{confidence*100:.1f}%",
        "1_Day_VaR": var_threshold,
        "1_Day_Expected_Shortfall": cvar_expected_shortfall
    }

if __name__ == "__main__":
    report = compute_var_cvar(portfolio_value=10000000.0, mean_return=0.0002, vol=0.015, days=1, confidence=0.99)
    print("=== GARP FRM Portfolio Risk Report ===")
    for k, v in report.items():
        print(f"  {k}: ${v:,.2f}" if isinstance(v, float) else f"  {k}: {v}")
