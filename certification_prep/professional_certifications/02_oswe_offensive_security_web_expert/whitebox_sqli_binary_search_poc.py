#!/usr/bin/env python3
"""
OSWE Proof of Concept: Automated Blind Time-Based SQLi Binary Search Extractor
Demonstrates deterministic white-box database schema extraction with logarithmic O(log N) probe complexity.
"""

class MockVulnerableEndpoint:
    def __init__(self, secret: str):
        self._secret = secret

    def query(self, pos: int, candidate_ascii: int) -> bool:
        if pos < 1 or pos > len(self._secret):
            return False
        actual_ascii = ord(self._secret[pos - 1])
        return actual_ascii > candidate_ascii

def extract_secret(endpoint: MockVulnerableEndpoint, length: int) -> str:
    recovered = []
    for pos in range(1, length + 1):
        low = 32
        high = 126
        while low <= high:
            mid = (low + high) // 2
            if endpoint.query(pos, mid):
                low = mid + 1
            else:
                high = mid - 1
        recovered.append(chr(low))
    return "".join(recovered)

if __name__ == "__main__":
    secret_token = "Flag{OSWE_Wh1teB0x_S0urc3_Aud1t}"
    app = MockVulnerableEndpoint(secret_token)
    extracted = extract_secret(app, len(secret_token))
    print(f"[*] Extracted Secret Token: {extracted}")
    assert extracted == secret_token, "Extraction mismatch!"
