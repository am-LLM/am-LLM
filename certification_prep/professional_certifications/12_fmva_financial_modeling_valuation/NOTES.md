# Financial Modeling & Valuation Analyst (FMVA) — Corporate Valuation Blueprint

## 1. Discounted Cash Flow (DCF) Valuation Architecture

```
                  UNLEVERED FREE CASH FLOW (FCFF) WATERFALL
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Earnings Before Interest & Taxes (EBIT)                                │
 │ Less: Cash Taxes Paid (EBIT * (1 - Tax Rate))                          │
 │ Add: Depreciation & Amortization (D&A - Non-Cash Charges)              │
 │ Less: Capital Expenditures (CapEx - Reinvestment in PP&E)             │
 │ Less: Change in Net Working Capital (ΔNWC = ΔCurrent Assets - ΔLiab)   │
 ├────────────────────────────────────────────────────────────────────────┤
 │ = UNLEVERED FREE CASH FLOW (FCFF)                                      │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Weighted Average Cost of Capital (WACC)

$$WACC = \left(\frac{E}{V} \times R_e\right) + \left(\frac{D}{V} \times R_d \times (1 - t)\right)$$

### Cost of Equity via Capital Asset Pricing Model (CAPM):
$$R_e = R_f + \beta \times (R_m - R_f)$$
Where:
* $R_f$ = Risk-Free Rate (e.g. 10-Year US Treasury yield).
* $\beta$ = Asset systematic equity risk covariance factor.
* $(R_m - R_f)$ = Equity Risk Premium (ERP).

### Terminal Value Calculation ($TV$):
1. **Gordon Growth Model**:
   $$TV_n = \frac{FCFF_{n+1}}{WACC - g} = \frac{FCFF_n \times (1 + g)}{WACC - g}$$
2. **Exit Multiple Method**:
   $$TV_n = \text{Terminal EBITDA}_n \times \text{EV/EBITDA Multiple}$$
