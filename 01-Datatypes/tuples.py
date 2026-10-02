# Creating a tuple

server = ("web01", "192.168.1.10", 80)

print(server)
print(type(server))

# Indexing
print(server[0])
print(server[1])

# Slicing
print(server[0:2])

# Length
print(len(server))

# Loop
for value in server:
    print(value)

# Check existence
if 80 in server:
    print("HTTP port found")

# Tuple unpacking

name, ip, port = server

print(name)
print(ip)
print(port)