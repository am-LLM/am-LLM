# Certified Information Systems Security Professional (CISSP) — Master Body of Knowledge

## 1. Domain 1: Security and Risk Management

```
               CONFIDENTIALITY, INTEGRITY, AVAILABILITY (CIA TRIAD)
                  ┌─────────────────────────────────┐
                  │         Risk Governance         │
                  │  Policies • Standards • Laws    │
                  └────────────────┬────────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
 ┌───────────────┐         ┌───────────────┐         ┌───────────────┐
 │Confidentiality│         │   Integrity   │         │ Availability  │
 │(Bell-LaPadula)│         │(Biba, Clark-W)│         │(Redundancy/BCM│
 └───────────────┘         └───────────────┘         └───────────────┘
```

### Quantitative Risk Analysis Equations
* **Single Loss Expectancy ($SLE$)**:
  $$SLE = \text{Asset Value (AV)} \times \text{Exposure Factor (EF)}$$
  *where $EF$ is the percentage of asset lost in an incident.*
* **Annualized Loss Expectancy ($ALE$)**:
  $$ALE = SLE \times \text{Annualized Rate of Occurrence (ARO)}$$
* **Cost-Benefit Analysis ($CBA$) of Safeguard**:
  $$\text{Value to Org} = (ALE_{\text{pre-control}} - ALE_{\text{post-control}}) - \text{Annual Cost of Safeguard (ACS)}$$

### Formal Access Control Models
1. **Bell-LaPadula (Confidentiality Focused - Military)**:
   * **Simple Security Property**: *No Read Up (NRU)* — A subject cannot read an object at a higher classification level.
   * **$\star$-Property (Star Property)**: *No Write Down (NWD)* — A subject at a higher clearance cannot write down to a lower security level (prevents data leakage).
   * **Discretionary Security Property**: Uses access matrix for DAC.
2. **Biba Model (Integrity Focused - Commercial/Financial)**:
   * **Simple Integrity Axiom**: *No Read Down (NRD)* — A subject cannot read lower integrity data (prevents corruption by untrusted sources).
   * **$\star$-Integrity Axiom**: *No Write Up (NWU)* — A subject cannot write to a higher integrity object.
3. **Clark-Wilson Model (Commercial Transactions)**:
   * Enforces Separation of Duties via Well-Formed Transactions (WFT) and Transformation Procedures (TPs) acting on Constrained Data Items (CDIs).
4. **Brewer-Nash (Chinese Wall)**:
   * Dynamically alters access permissions based on user's previous actions to avoid Conflict of Interest (COI).

---

## 2. Domain 3: Security Architecture and Engineering

### Cryptographic Foundations
* **Symmetric Encryption**: AES (Rijndael, 128/192/256-bit block size 128-bit), ChaCha20.
  * Modes of Operation: CBC (requires IV, sequential), GCM (authenticated encryption with AEAD, parallelizable), CTR.
* **Asymmetric Cryptography**: RSA (Factoring semi-primes), ECC (Elliptic Curve Discrete Logarithm Problem - ECDSA, Ed25519).
* **Zero-Knowledge Proofs & Post-Quantum Algorithms**: NIST FIPS 203 ML-KEM (Kyber lattice-based key encapsulation) and FIPS 204 ML-DSA (Dilithium digital signatures).

---

## 3. Domain 4: Communication and Network Security

### OSI Model vs TCP/IP Mapping & Attacks
| Layer # | OSI Layer | Protocol Unit | Security Threats & Controls |
|---|---|---|---|
| **7** | Application | Data | XSS, SQLi, CSRF, WAF, API Gateways |
| **6** | Presentation | Data | Encoding flaws, TLS termination, ASN.1 parsing |
| **5** | Session | Data | Session hijacking, RPC authentication |
| **4** | Transport | Segment (TCP) / Datagram (UDP) | SYN Flood, RST Injection, TLS/DTLS, Port Filtering |
| **3** | Network | Packet | IP Spoofing, ICMP redirect, IPsec (AH/ESP in Tunnel/Transport) |
| **2** | Data Link | Frame | ARP Poisoning, MAC Flooding, 802.1X, DHCP Snooping |
| **1** | Physical | Bits | Wiretapping, TEMPEST emissions, Faraday cages |

---

## 4. Domain 7 & 8: Security Operations & Software Development

* **Disaster Recovery Strategy**:
  * **Hot Site**: Fully operational real-time mirrored environment ($RTO \approx 0$).
  * **Warm Site**: Hardware provisioned, requires data restore ($RTO \approx \text{hours}$).
  * **Cold Site**: Facility space/power available, no pre-installed hardware ($RTO \approx \text{days/weeks}$).
* **Software Development Lifecycle (SDLC)**:
  * Static Application Security Testing (SAST) $\to$ Dynamic Application Security Testing (DAST) $\to$ Software Composition Analysis (SCA) $\to$ Interactive Application Security Testing (IAST).
