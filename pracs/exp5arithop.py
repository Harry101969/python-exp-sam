# Takes two numbers and performs basic arithmetic operations
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b==0:
    print("Division: undefined")
else:
   print("Division:", a / b )
print("Modulous: ",a%b)