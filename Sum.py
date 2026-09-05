import sys

if len(sys.argv) == 3:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

result = num1 + num2

print("Sum =", result)