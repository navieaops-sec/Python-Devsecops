# Python Sets

A set is an unordered collection of unique values.

ips = {"10.0.0.1", "10.0.0.2"}

#Characteristics:
Unordered
Mutable
No duplicate values
No indexing
Useful for uniqueness

#Duplicate Removal

ips = {"10.0.0.1", "10.0.0.1"}

print(ips)

Output:

{'10.0.0.1'}

#Important Set Operations

1.Union : Combines both sets.

a | b

2.Intersection : Returns common values.

a & b

3.Difference : Returns values present in the first set but not second.

a - b

#DevSecOps Example

Sets are useful when comparing:

Vulnerabilities from two scans
IP addresses
Open ports
Docker images
Security findings

Example:

scan1 = {"CVE-1234", "CVE-5678"}
scan2 = {"CVE-5678", "CVE-9999"}
print(scan1 & scan2)
This identifies vulnerabilities common to both scans.

![alt text](image.png)