def calculator(a, b, operation="add"):
if operation == "add":
return a + b
elif operation == "subtract":
return a - b
elif operation == "multiply":
return a * b
elif operation == "divide":
if b == 0:
return "Error: Division by zero is not allowed."
return a / b
else:
return "Invalid operation! Please choose add, subtract, multiply, or divide."
# Example Usage
print(calculator(10, 5)) # Default addition
print(calculator(10, 5, "subtract")) # Subtraction
print(calculator(10, 5, "multiply")) # Multiplication
print(calculator(10, 5, "divide")) # Division
print(calculator(10, 5, "power")) # Invalid operation
