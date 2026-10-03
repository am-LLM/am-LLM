# CISSP 8-Domain Enterprise Security Architecture Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: (ISC)² CISSP Common Body of Knowledge (CBK). Security Models, Cryptography, BCP/DRP, and Identity Governance.

---

## 1. Formal Security Models & State Machine Controls

### 1.1 Bell-LaPadula Model (Confidentiality)
* **Simple Security Property (ss-property)**: *No Read Up (NRU)* — A subject at a lower clearance cannot read an object at a higher classification.
* **$\star$-Property (Star Property)**: *No Write Down (NWD)* — A subject at a higher clearance cannot write down to a lower security level.

### 1.2 Biba Integrity Model
* **Simple Integrity Axiom**: *No Read Down (NRD)* — A subject cannot read lower-integrity data (prevents contamination).
* **$\star$-Integrity Axiom**: *No Write Up (NWU)* — A subject cannot write data to a higher-integrity object.

---

## 2. Quantitative Risk Assessment Calculations

* **Asset Value (AV)**: Total economic worth of the asset.
* **Exposure Factor (EF)**: Percentage of asset lost in a realized threat.
* **Single Loss Expectancy (SLE)**:
  $$	ext{SLE} = 	ext{AV} 	imes 	ext{EF}$$
* **Annualized Rate of Occurrence (ARO)**: Estimated frequency per year.
* **Annualized Loss Expectancy (ALE)**:
  $$	ext{ALE} = 	ext{SLE} 	imes 	ext{ARO}$$
* **Cost-Benefit Analysis (CBA) of Security Safeguard**:
  $$	ext{CBA} = (	ext{ALE}_{	ext{prior}} - 	ext{ALE}_{	ext{post}}) - 	ext{ACS}$$
  *(where ACS is Annual Cost of Safeguard)*
