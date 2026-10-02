# Python Type Conversion

Type conversion means changing a value from one data type to another.

## Common Functions


int()
float()
str()
list()
tuple()
set()
dict()
String to Integer
port = "443"

port = int(port)
String to Float
cpu = "75.5"

cpu = float(cpu)
Integer to String
count = 10

count = str(count)
List to Set

Useful for removing duplicates.

ips = ["10.0.0.1", "10.0.0.1"]

unique_ips = set(ips)
String to List
servers = "web01,web02,web03"

servers = servers.split(",")

Result:

["web01", "web02", "web03"]

#DevSecOps Importance

Type conversion is frequently required when working with:

Environment variables
CLI arguments
API responses
JSON data
Configuration files
AWS CLI output
Kubernetes commands
CI/CD variables

For example, environment variables are normally strings:

import os

port = os.getenv("PORT")

port = int(port)
Interview Question
Why is type conversion important?

External data often comes in as strings. Type conversion allows Python programs to perform the correct operations on that data.

![alt text](image.png)