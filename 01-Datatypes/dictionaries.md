 Python Dictionaries:

A dictionary stores data as key-value pairs.

server = {
    "name": "web01",
    "ip": "192.168.1.10",
    "port": 443
}

#Structure : key → value

Example:

name → web01
ip   → 192.168.1.10
port → 443

#Characteristics:
Mutable
Stores key-value pairs
Keys must be unique
Values can be duplicated
Fast lookup using keys
Accessing Values

server["ip"]

or:

server.get("ip")

#Common Methods
keys()
values()
items()
get()
update()
pop()

#DevSecOps Example

Dictionaries are extremely useful for structured security data.

vulnerability = {
    "cve": "CVE-2025-1234",
    "severity": "HIGH",
    "component": "nginx"
}

They are commonly used when processing:

JSON
API responses
AWS responses
Kubernetes data
Security scanner output
Configuration files
Interview Question
List vs Dictionary

List:
servers = ["web01", "web02"]

Dictionary:
server = {
    "name": "web01",
    "ip": "10.0.0.5"
}

List → access using index.

Dictionary → access using key.