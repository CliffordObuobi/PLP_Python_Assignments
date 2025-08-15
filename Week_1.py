# Basic Calculator Program

# Get two numbers from the user
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

# Convert the input to numbers (decimals)
num1 = float(number1)
num2 = float(number2)

# Ask what operation to do
operation = input("Enter operation (+, -, *, /): ")

# Do the math based on the operation
if operation == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)

if operation == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)

if operation == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)

if operation == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)

# If the user didn't enter a valid operation
if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print("Invalid operation. Please use +, -, *, or /")