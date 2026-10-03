# GARP Financial Risk Manager (FRM Part I & II) — Quantitative Risk Architecture

## 1. Value-at-Risk (VaR) & Expected Shortfall (ES / CVaR)

```
                     LOSS DISTRIBUTION & VALUE-AT-RISK
              Probability Density
                      │
                      │         Normal Distribution / Fat-Tailed
                      │                   ▲
                      │                  ╱ ╲
                      │                 ╱   ╲
                      │                ╱     ╲
                      │   VaR (α=99%) ╱       ╲
                      │        │     ╱         ╲
       Expected       │        │    ╱           ╲
    Shortfall (CVaR)  │  Tail  ▼   ╱             ╲
   ◄──────────────────┼─────────┬─╱               ╲───────────────► Loss/Profit
                      └─────────┴─────────────────────────────────
```

### Parametric (Delta-Normal) Value-at-Risk:
$$\text{VaR}_{\alpha} = -(\mu \Delta t - Z_{\alpha} \sigma \sqrt{\Delta t}) \times V$$

Where:
* $V$ = Portfolio Value.
* $Z_{\alpha}$ = Standard normal inverse critical value ($Z_{0.95} = 1.645$, $Z_{0.99} = 2.326$).
* $\sigma$ = Asset daily volatility.
* $\Delta t$ = Holding period time horizon (e.g. 10 days via Basel square root of time rule: $\text{VaR}_{10d} = \text{VaR}_{1d} \times \sqrt{10}$).

### Expected Shortfall ($ES_{\alpha}$ / Conditional VaR):
Expected loss given that the loss exceeds the $\text{VaR}_{\alpha}$ threshold (Subadditive and Coherent Risk Measure):
$$ES_{\alpha} = \mathbb{E}[L \mid L > \text{VaR}_{\alpha}]$$

---

## 2. Black-Scholes-Merton Option Pricing & Greeks
* **Call Option Price**: $C(S, t) = S_t N(d_1) - K e^{-r(T-t)} N(d_2)$
* **Delta ($\Delta$)**: $\frac{\partial C}{\partial S} = N(d_1)$
* **Gamma ($\Gamma$)**: $\frac{\partial^2 C}{\partial S^2} = \frac{N'(d_1)}{S \sigma \sqrt{T-t}}$
* **Vega ($\nu$)**: $\frac{\partial C}{\partial \sigma} = S \sqrt{T-t} N'(d_1)$
* **Theta ($\Theta$)**: Time decay of derivative value.
