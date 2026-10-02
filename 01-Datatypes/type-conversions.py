# String to integer

port = "443"

print(port)
print(type(port))

port = int(port)

print(port)
print(type(port))


# String to float

cpu = "75.5"

cpu = float(cpu)

print(cpu)
print(type(cpu))


# Integer to string

server_count = 10

server_count = str(server_count)

print(server_count)
print(type(server_count))


# List to set

ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1"]

unique_ips = set(ips)

print(unique_ips)


# Set to list

unique_ips = list(unique_ips)

print(unique_ips)


# String to list

servers = "web01,web02,web03"

server_list = servers.split(",")

print(server_list)


# DevSecOps example

port = "8080"

if int(port) > 1024:
    print("Non-privileged port")