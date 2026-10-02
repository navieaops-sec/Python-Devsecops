### Exercise 1 — IP extraction

import re

log = """
Server1: 192.168.1.10
Server2: 10.0.0.5
Server3: 172.16.0.20
"""

ips = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", log)


print(ips)
## Exercise 2 — CVE Extraction
import re

text = """
Found CVE-2024-1234 and CVE-2025-5678 during security scan
"""

cves = re.findall(r"CVE-\d{4}-\d+", text)

print(cves)

### Exercise 3 — Log Filtering
import re

log = """
INFO Application started
ERROR Database connection failed
WARNING High CPU usage
INFO User logged in
ERROR Authentication failed
"""

lines = re.findall(r"^(?:ERROR|WARNING).*$", log, re.MULTILINE)

for line in lines:
    print(line)
    
###Exercise 4 — Secret Masking
import re

text = "password=MySecret123"

masked = re.sub(
    r"password=\S+",
    "password=REDACTED",
    text
)

print(masked)

###Exercise 5 — Failed SSH Detection
import re

log = """
Failed password for root from 192.168.1.20
Accepted password for navya from 10.0.0.5
Failed password for admin from 172.16.0.10
"""

failed_ips = re.findall(
    r"Failed password.*from\s+(\b(?:\d{1,3}\.){3}\d{1,3}\b)",
    log
)

print(failed_ips)