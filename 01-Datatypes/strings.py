# ==========================================
# Python Strings - Built-in Practice
# DevSecOps Automation Learning
# ==========================================
# ------------------------------------------
# 1. To get the datatype of Strings
# ------------------------------------------
username = "navya"
repository = "enterprise-devsecops-platform"
environment = "production"

print(type(username))

# ------------------------------------------
# 2. Creating Strings
# ------------------------------------------

name = "Navya"
environment = 'production'
message = """Security scan completed successfully."""

print(name)
print(environment)
print(message)

# ------------------------------------------
# 3. Basic String Operations
# ------------------------------------------

text = "DevSecOps"

print(text)
print(len(text))

# Indexing
print(text[0])
print(text[-1])

# Slicing
print(text[0:5])
print(text[:5])
print(text[5:])

# ------------------------------------------
# 4. Case Conversion
# ------------------------------------------

text = "devsecops automation"

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())


# ------------------------------------------
# 5. Removing Whitespace
# ------------------------------------------

environment = "   production   "

print(environment.strip())
print(environment.lstrip())
print(environment.rstrip())


# ------------------------------------------
# 6. Searching Inside Strings
# ------------------------------------------

log_message = "ERROR: Docker container failed"

print("ERROR" in log_message)
print("WARNING" in log_message)

print(log_message.find("Docker"))
print(log_message.count("container"))


# ------------------------------------------
# 7. Checking String Content
# ------------------------------------------

value = "12345"

print(value.isdigit())
print(value.isalpha())
print(value.isalnum())
print(value.isspace())


# ------------------------------------------
# 8. startswith() and endswith()
# ------------------------------------------

filename = "security_report.json"

print(filename.startswith("security"))
print(filename.endswith(".json"))


# ------------------------------------------
# 9. split()
# ------------------------------------------

tools = "Docker,Kubernetes,Terraform,Trivy"

tool_list = tools.split(",")

print(tool_list)


# ------------------------------------------
# 10. join()
# ------------------------------------------

tools = ["Docker", "Kubernetes", "Terraform"]

result = ", ".join(tools)

print(result)


# ------------------------------------------
# 11. replace()
# ------------------------------------------

message = "Environment: testing"

updated_message = message.replace("testing", "production")

print(updated_message)


# ------------------------------------------
# 12. f-strings
# ------------------------------------------

environment = "production"
status = "SUCCESS"

message = f"Deployment to {environment}: {status}"

print(message)


# ------------------------------------------
# 13. not in
# ------------------------------------------

log = "Deployment completed successfully"

if "ERROR" not in log:
    print("No error found")


# ------------------------------------------
# 14. DevSecOps Example
# Docker Image Tag Validation
# ------------------------------------------

image_name = "backend-app:v1.2.0"

if image_name.endswith(":latest"):
    print("Warning: latest tag should not be used")
else:
    print("Versioned Docker image tag detected")


# ------------------------------------------
# 15. DevSecOps Example
# Log Processing
# ------------------------------------------

log = "2026-10-01 ERROR Kubernetes pod failed"

if "ERROR" in log:
   print("Security/operations team should investigate this log")


# ------------------------------------------
# 16. DevSecOps Example
# Environment Normalization
# ------------------------------------------

environment = "  PRODUCTION  "

environment = environment.strip().lower()

print(environment)