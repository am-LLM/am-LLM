# AWS Solutions Architect Professional (SAP-C02) Architecture Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: Multi-Region Active-Active Architectures, Route 53 ARC, DynamoDB Global Tables, and KMS Envelope Encryption.

---

## 1. Envelope Encryption with AWS KMS (2-Tier Key Hierarchy)

```
[ AWS KMS HSM ] ──(Generates Plaintext + Encrypted DEK)──▶ [ Application Server ]
                                                                   │
                                                            Encrypts Payload
                                                                   ▼
[ S3 Storage Bucket ] ◀── [ Ciphertext Data + Encrypted Data Key (DEK) ]
```
