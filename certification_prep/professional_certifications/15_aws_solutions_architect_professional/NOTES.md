# AWS Certified Solutions Architect - Professional (SAP-C02) Architecture Guide

## 1. Multi-Region Active-Active & Fault-Tolerant Patterns

```
                 MULTI-REGION ACTIVE-ACTIVE DISASTER RECOVERY
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Route 53 (Latency / Geolocation Routing with Health Check DNS Failover)│
 └───────────────────┬────────────────────────────────┬───────────────────┘
                     │                                │
                     ▼                                ▼
 ┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
 │ Region 1 (us-east-1)                 │  │ Region 2 (eu-west-1)                 │
 │ • ALB + Auto Scaling Multi-AZ ECS    │  │ • ALB + Auto Scaling Multi-AZ ECS    │
 │ • DynamoDB Global Tables (Bi-dir rep)│  │ • DynamoDB Global Tables (Bi-dir rep)│
 │ • S3 Cross-Region Replication (CRR)  │  │ • S3 Cross-Region Replication (CRR)  │
 │ • Aurora Global Database (<1s rep)   │  │ • Aurora Global Read Replica (Fast-Pr│
 └──────────────────────────────────────┘  └──────────────────────────────────────┘
```

---

## 2. Security, Cryptography & KMS Architecture
* **AWS KMS Envelope Encryption**:
  1. Client requests data key from KMS (`GenerateDataKey` with Customer Master Key - CMK).
  2. KMS returns Plaintext Data Encryption Key ($DEK$) + Ciphertext $DEK$ (encrypted under CMK).
  3. Client encrypts plaintext payload using Plaintext $DEK$ with AES-256-GCM.
  4. Client immediately zeroes Plaintext $DEK$ from RAM and stores Ciphertext $DEK$ alongside ciphertext payload.
