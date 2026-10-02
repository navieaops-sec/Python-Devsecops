Lists

This is **very important for DevSecOps** because you'll constantly work with collections of servers, vulnerabilities, containers, files, etc.

A list is an ordered and mutable collection.
eg: servers = ["web01", "web02", "db01"]

#Characteristics :
Ordered
Mutable
Allows duplicates
Supports indexing
Supports slicing
Can contain different data types

#Indexing

The first element has index 0 : servers[0]
Negative indexing starts from the end:servers[-1]
-1 means the last element.

#Slicing

servers[0:2]This means: Start at index 0 and stop before index 2.


DevSecOps Examples

Lists can store:

Vulnerabilities
IP addresses
Server names
Docker containers
Kubernetes pods
File names
Security findings

Example:

vulnerabilities = ["CVE-1234", "CVE-5678"]

for vuln in vulnerabilities:
    print(vuln)
Interview Question
List vs String?

A string stores text:

name = "server"

A list stores multiple values:

servers = ["web01", "web02"]

Lists are mutable, while strings are immutable.

![alt text](image-2.png)