None

# None represents absence of a value

result = None

print(result)
print(type(result))
result = None

Its type is:

<class 'NoneType'>
Checking None

Use:

is None

Example:

if result is None:
    print("No result")

Prefer is None instead of:

result == None
DevSecOps Examples

None can represent:

No scan result
No vulnerability
Missing configuration
Missing API response
Optional value
Resource not found

Example:

ip = None

if ip is None:
    print("IP address unavailable")
Interview Question
What is None?

None is a special Python object representing the absence of a value.
![alt text](image.png)