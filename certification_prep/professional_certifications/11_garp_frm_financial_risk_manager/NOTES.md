# GARP FRM® Quantitative Risk & Portfolio Volatility Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: GARP FRM Part I & II. Parametric VaR, Historical Simulation, Expected Shortfall (CVaR), and Merton Credit Risk.

---

## 1. Value at Risk (VaR) & Expected Shortfall (CVaR)

* **Parametric Normal VaR**:
  $$	ext{VaR}_{lpha} = \mu - Z_{lpha} 	imes \sigma 	imes \sqrt{\Delta t}$$
  *(For 99% 1-day confidence, $Z_{0.99} pprox 2.326$)*

* **Expected Shortfall (Conditional VaR)**:
  $$	ext{ES}_{lpha} = E[L \mid L > 	ext{VaR}_{lpha}]$$
