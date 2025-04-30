import re

email = input("Enter email: ")
phone = input("Enter phone: ")

if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email")
else:
    print("Invalid email")

if re.match(r"\d{10}", phone):
    print("Valid phone")
else:
    print("Invalid phone")
