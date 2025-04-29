try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
# so what is exception handling is that it lets the code execute completely without breaking in the middle of the execution and without throwing errors!!