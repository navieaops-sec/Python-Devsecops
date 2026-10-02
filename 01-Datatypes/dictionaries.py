# Creating a dictionary

server = {
    "name": "web01",
    "ip": "192.168.1.10",
    "port": 443,
    "environment": "production"
}

print(server)
print(type(server))

# Access values
print(server["name"])
print(server["ip"])

# get()
print(server.get("port"))

# Add new key
server["status"] = "running"

# Update value
server["port"] = 8443

print(server)

# Keys
print(server.keys())

# Values
print(server.values())

# Items
print(server.items())

# Loop
for key, value in server.items():
    print(key, ":", value)

# Security example

vulnerability = {
    "cve": "CVE-2025-1234",
    "severity": "HIGH",
    "component": "nginx",
    "status": "OPEN"
}

print(vulnerability["severity"])