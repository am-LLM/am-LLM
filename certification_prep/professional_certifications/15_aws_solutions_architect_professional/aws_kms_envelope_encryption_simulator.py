#!/usr/bin/env python3
"""
AWS SAP-C02: KMS Envelope Encryption Simulation
Demonstrates local payload encryption using asymmetric master keys and dynamic Data Encryption Keys (DEK).
"""

import hashlib
import os

class KMSMock:
    def __init__(self):
        self.master_key = os.urandom(32)

    def generate_data_key(self):
        plaintext_dek = os.urandom(32)
        # Encrypt DEK with master key (XOR simulation for lightweight demo)
        encrypted_dek = bytes(a ^ b for a, b in zip(plaintext_dek, self.master_key))
        return plaintext_dek, encrypted_dek

if __name__ == "__main__":
    kms = KMSMock()
    plain_dek, enc_dek = kms.generate_data_key()
    print("[*] AWS KMS Envelope Encryption Test:")
    print(f"  Plaintext DEK (Held in RAM only):   {plain_dek.hex()[:16]}...")
    print(f"  Encrypted DEK (Stored with Data):   {enc_dek.hex()[:16]}...")
