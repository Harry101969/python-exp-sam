# Store and display records of 5 students with their roll numbers
records = []

# Input details for 5 students
for i in range(5):
    print(f"\nEnter details for student {i + 1}:")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    records.append((name, roll))  # Store as tuple (name, roll)

# Display all student records
print("\n--- Student Records ---")
for student in records:
    print("Name:", student[0], "| Roll No:", student[1])
