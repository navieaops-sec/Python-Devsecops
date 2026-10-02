# None represents absence of a value

result = None

print(result)
print(type(result))

## Checking None

if result is None:
    print("No result available")

# Function returning None

def scan_server():
    print("Scanning server...")
    return None

result = scan_server()

if result is None:
    print("Scan returned no result")

# DevSecOps example

vulnerability = None

if vulnerability is None:
    print("No vulnerability found")