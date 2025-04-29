students = []

for i in range(2):
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    branch = input("Enter branch: ")
    students.append({'Name': name, 'Roll': roll, 'Branch': branch})

print("\nStudent Records:")
for s in students:
    print(f"Name: {s['Name']}, Roll: {s['Roll']}, Branch: {s['Branch']}")
