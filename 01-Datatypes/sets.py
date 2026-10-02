# Creating a set

ips = {
    "10.0.0.1",
    "10.0.0.2",
    "10.0.0.1"
}

print(ips)

# Duplicates are automatically removed

# Add
ips.add("10.0.0.3")
print(ips)

# Remove
ips.remove("10.0.0.2")
print(ips)

# Membership
if "10.0.0.1" in ips:
    print("IP found")

# Set operations

scan1 = {"10.0.0.1", "10.0.0.2", "10.0.0.3"}
scan2 = {"10.0.0.2", "10.0.0.3", "10.0.0.4"}

print("Union:", scan1 | scan2)
print("Intersection:", scan1 & scan2)
print("Difference:", scan1 - scan2)