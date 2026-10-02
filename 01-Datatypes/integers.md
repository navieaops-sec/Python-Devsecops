 Python Numbers

Python mainly uses:

- int
- float
- complex

## Integer

Whole numbers.

```python
servers = 10
Float

Numbers containing decimal values.

cpu_usage = 75.5
Arithmetic Operators
Operator	Meaning
+	Addition
-	Subtraction
*	Multiplication
/	Division
//	Floor division
%	Modulus
**	Power
DevSecOps Example

Numbers are commonly used for:

CPU usage
Memory usage
Disk usage
HTTP status counts
Vulnerability counts
Scan duration
Deployment statistics
critical = 5
high = 10

total = critical + high
print(total)
Interview Question
What is the difference between / and //?

/ returns normal division.

10 / 3
# 3.3333333333333335

// performs floor division.

10 // 3
# 3


#####list methods
list methods in Python.

Why are they called methods?

A method is a function that belongs to an object/data type and is called using the dot . notation.

For example:

servers = ["web01", "web02"]

servers.append("web03")

Here:

servers → list object
append() → list method
. → used to access the method
Common List Methods
Method	What it does	Example
append()	Adds an item at the end	servers.append("web03")
insert()	Adds an item at a specific position	servers.insert(1, "api01")
remove()	Removes a specific value	servers.remove("web02")
pop()	Removes and returns an item	servers.pop()
sort()	Sorts the list	servers.sort()
reverse()	Reverses the list	servers.reverse()
clear()	Removes all items	servers.clear()

🚀Important interview distinction

Don't call them just functions.

❌ append() is a Python function
✅ append() is a list method

But len() is a built-in function:

len(servers)

So remember:

List methods → list.append(), list.remove(), list.sort()
Built-in functions → len(), print(), type(), int(), str()

![alt text](image.png)