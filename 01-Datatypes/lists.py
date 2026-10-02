

# Creating a list

servers = ["web01", "web02", "db01"]

print(servers)
print(type(servers))

# Indexing
print(servers[0])
print(servers[1])
print(servers[-1])

# Slicing
print(servers[0:2])

# Adding
servers.append("web03")
print(servers)

# Insert
servers.insert(1, "api01")
print(servers)

# Remove
servers.remove("db01")
print(servers)

# Pop
server = servers.pop()
print(server)
print(servers)

# Length
print(len(servers))

# Loop
for server in servers:
    print(server)

# Check existence
if "web01" in servers:
    print("web01 found")

# Security example
vulnerabilities = [
    "CVE-2024-1234",
    "CVE-2025-5678",
    "CVE-2025-9999"
]

for vulnerability in vulnerabilities:
    print(f"Found: {vulnerability}")

print(f"Total vulnerabilities: {len(vulnerabilities)}")