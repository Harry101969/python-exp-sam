############################################################
# 1. Personalised Greeting Generator
############################################################

def greeting_generator():
    """
    A simple program that asks for user's name and greets them
    with a personalized message.
    """
    print("===== Personalised Greeting Generator =====")
    
    # Get user input
    name = input("Please enter your name: ")
    
    # Generate greeting based on name
    print(f"\nHello, {name}! Welcome to Python Programming.")
    print(f"It's great to have you here, {name}!")
    
    # Ask about their day for more personalization
    feeling = input("\nHow are you feeling today? ")
    print(f"I'm glad to hear you're feeling {feeling}, {name}!")
    
    print("\nThank you for using the Personalised Greeting Generator!")

# Call the function to run this experiment
print("\nEXPERIMENT 1: PERSONALISED GREETING GENERATOR")
greeting_generator()
print("\n" + "="*50 + "\n")


############################################################
# 2. Calculate order of geometric fig
############################################################

def geometric_figure_order():
    """
    A program to calculate the order of geometric figures.
    Order = Number of sides or vertices
    """
    print("===== Geometric Figure Order Calculator =====")
    print("\nThis program calculates the order of geometric figures.")
    print("The order is determined by the number of sides or vertices.")
    
    # Dictionary of common geometric figures and their orders
    figures = {
        "triangle": 3,
        "square": 4,
        "pentagon": 5,
        "hexagon": 6,
        "heptagon": 7,
        "octagon": 8,
        "nonagon": 9,
        "decagon": 10
    }
    
    # Display available figures
    print("\nAvailable Geometric Figures:")
    for figure in figures:
        print(f"- {figure.capitalize()}")
    
    # Get user's choice
    choice = input("\nEnter the name of a geometric figure: ").lower()
    
    # Calculate and display the order
    if choice in figures:
        print(f"\nThe order of a {choice} is {figures[choice]}.")
        print(f"This means a {choice} has {figures[choice]} sides and {figures[choice]} vertices.")
    elif choice.isdigit():
        # Allow the user to enter a number of sides directly
        sides = int(choice)
        if sides < 3:
            print("\nA geometric figure must have at least 3 sides.")
        else:
            print(f"\nA geometric figure with {sides} sides is called a ", end="")
            if sides == 3:
                print("triangle.")
            elif sides == 4:
                print("quadrilateral (or square/rectangle).")
            else:
                print(f"{sides}-gon.")
            print(f"Its order is {sides}.")
    else:
        print("\nSorry, that geometric figure is not in our database.")
        custom_sides = input("Enter the number of sides for this figure: ")
        if custom_sides.isdigit() and int(custom_sides) >= 3:
            print(f"\nA {choice} with {custom_sides} sides has an order of {custom_sides}.")
        else:
            print("\nInvalid input. A geometric figure must have at least 3 sides.")
    
    print("\nThank you for using the Geometric Figure Order Calculator!")

# Call the function to run this experiment
print("\nEXPERIMENT 2: CALCULATE ORDER OF GEOMETRIC FIGURE")
geometric_figure_order()
print("\n" + "="*50 + "\n")


############################################################
# 3. Calculate Gross Salary
############################################################

def calculate_gross_salary():
    """
    A program to calculate gross salary based on basic salary
    and additional allowances.
    """
    print("===== Gross Salary Calculator =====")
    
    try:
        # Get basic salary from user
        basic_salary = float(input("\nEnter your basic salary: ₹"))
        
        # Calculate allowances
        da = 0.40 * basic_salary  # Dearness Allowance: 40% of basic
        hra = 0.15 * basic_salary  # House Rent Allowance: 15% of basic
        ta = 0.10 * basic_salary  # Travel Allowance: 10% of basic
        
        # Calculate gross salary
        gross_salary = basic_salary + da + hra + ta
        
        # Display the results with proper formatting
        print("\n===== Salary Details =====")
        print(f"Basic Salary: ₹{basic_salary:.2f}")
        print(f"Dearness Allowance (40%): ₹{da:.2f}")
        print(f"House Rent Allowance (15%): ₹{hra:.2f}")
        print(f"Travel Allowance (10%): ₹{ta:.2f}")
        print("-" * 30)
        print(f"Gross Salary: ₹{gross_salary:.2f}")
        
    except ValueError:
        print("\nError: Please enter a valid number for the salary amount.")
    
    print("\nThank you for using the Gross Salary Calculator!")

# Call the function to run this experiment
print("\nEXPERIMENT 3: CALCULATE GROSS SALARY")
calculate_gross_salary()
print("\n" + "="*50 + "\n")


############################################################
# 4. Calculating Simple Interest
############################################################

def calculate_simple_interest():
    """
    A program to calculate simple interest based on
    principal amount, rate of interest, and time period.
    """
    print("===== Simple Interest Calculator =====")
    
    try:
        # Get input values from user
        principal = float(input("\nEnter the principal amount: ₹"))
        rate = float(input("Enter the annual interest rate (%): "))
        time = float(input("Enter the time period (in years): "))
        
        # Calculate simple interest: SI = P * R * T / 100
        simple_interest = (principal * rate * time) / 100
        
        # Calculate the total amount
        total_amount = principal + simple_interest
        
        # Display the results
        print("\n===== Interest Calculation =====")
        print(f"Principal Amount: ₹{principal:.2f}")
        print(f"Annual Interest Rate: {rate}%")
        print(f"Time Period: {time} years")
        print("-" * 30)
        print(f"Simple Interest: ₹{simple_interest:.2f}")
        print(f"Total Amount after {time} years: ₹{total_amount:.2f}")
        
    except ValueError:
        print("\nError: Please enter valid numbers for all fields.")
    
    print("\nThank you for using the Simple Interest Calculator!")

# Call the function to run this experiment
print("\nEXPERIMENT 4: CALCULATING SIMPLE INTEREST")
calculate_simple_interest()
print("\n" + "="*50 + "\n")


############################################################
# 5. Arithmetic Operations
############################################################

def arithmetic_operations():
    """
    A program to perform basic arithmetic operations on two numbers.
    """
    print("===== Arithmetic Operations Calculator =====")
    
    try:
        # Get two numbers from user
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform arithmetic operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        
        # Handle division by zero error
        if num2 == 0:
            division = "Error: Cannot divide by zero"
            modulus = "Error: Cannot divide by zero"
            floor_division = "Error: Cannot divide by zero"
        else:
            division = num1 / num2
            modulus = num1 % num2
            floor_division = num1 // num2
        
        # Calculate exponentiation
        exponentiation = num1 ** num2
        
        # Display the results
        print("\n===== Results =====")
        print(f"{num1} + {num2} = {addition}")
        print(f"{num1} - {num2} = {subtraction}")
        print(f"{num1} * {num2} = {multiplication}")
        
        if isinstance(division, str):
            print(f"{num1} / {num2} = {division}")
            print(f"{num1} % {num2} = {modulus}")
            print(f"{num1} // {num2} = {floor_division}")
        else:
            print(f"{num1} / {num2} = {division}")
            print(f"{num1} % {num2} = {modulus}")
            print(f"{num1} // {num2} = {floor_division}")
        
        print(f"{num1} ** {num2} = {exponentiation}")
        
    except ValueError:
        print("\nError: Please enter valid numbers.")
    
    print("\nThank you for using the Arithmetic Operations Calculator!")

# Call the function to run this experiment
print("\nEXPERIMENT 5: ARITHMETIC OPERATIONS")
arithmetic_operations()
print("\n" + "="*50 + "\n")


############################################################
# 6. Task List Manager
############################################################

def task_list_manager():
    """
    A simple task list manager to add, view, and mark tasks as complete.
    """
    print("===== Task List Manager =====")
    
    # Initialize an empty list to store tasks
    tasks = []
    
    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Remove a task")
        print("5. Exit")
        
        # Get user's choice
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            # Add a new task
            task = input("\nEnter a new task: ")
            tasks.append({"task": task, "completed": False})
            print(f"Task '{task}' added successfully!")
            
        elif choice == '2':
            # View all tasks
            if not tasks:
                print("\nNo tasks found. Your task list is empty.")
            else:
                print("\n===== Your Tasks =====")
                for i, task in enumerate(tasks):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i+1}. [{status}] {task['task']}")
            
        elif choice == '3':
            # Mark a task as complete
            if not tasks:
                print("\nNo tasks found. Your task list is empty.")
            else:
                print("\n===== Your Tasks =====")
                for i, task in enumerate(tasks):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i+1}. [{status}] {task['task']}")
                
                try:
                    task_num = int(input("\nEnter the task number to mark as complete: "))
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num-1]["completed"] = True
                        print(f"Task '{tasks[task_num-1]['task']}' marked as complete!")
                    else:
                        print("Invalid task number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
        elif choice == '4':
            # Remove a task
            if not tasks:
                print("\nNo tasks found. Your task list is empty.")
            else:
                print("\n===== Your Tasks =====")
                for i, task in enumerate(tasks):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{i+1}. [{status}] {task['task']}")
                
                try:
                    task_num = int(input("\nEnter the task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num-1)
                        print(f"Task '{removed_task['task']}' removed successfully!")
                    else:
                        print("Invalid task number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
        elif choice == '5':
            # Exit the program
            print("\nThank you for using the Task List Manager!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

# Call the function to run this experiment
print("\nEXPERIMENT 6: TASK LIST MANAGER")
task_list_manager()
print("\n" + "="*50 + "\n")


############################################################
# 7. Student Enrollment Manager
############################################################

def student_enrollment_manager():
    """
    A program to manage student enrollments in courses.
    """
    print("===== Student Enrollment Manager =====")
    
    # Initialize data structures
    students = []
    courses = ["Python Programming", "Data Structures", "Database Management", 
              "Web Development", "Machine Learning"]
    
    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Enroll a new student")
        print("2. View all students")
        print("3. View enrollments by course")
        print("4. Remove a student")
        print("5. Exit")
        
        # Get user's choice
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            # Enroll a new student
            name = input("\nEnter student name: ")
            roll_number = input("Enter roll number: ")
            
            # Check if roll number already exists
            existing_roll_numbers = [s["roll_number"] for s in students]
            if roll_number in existing_roll_numbers:
                print(f"Error: Roll number {roll_number} already exists. Please use a different roll number.")
                continue
            
            # Display available courses
            print("\nAvailable Courses:")
            for i, course in enumerate(courses):
                print(f"{i+1}. {course}")
            
            # Select courses
            enrolled_courses = []
            try:
                num_courses = int(input("\nHow many courses do you want to enroll in? "))
                if num_courses < 1 or num_courses > len(courses):
                    print(f"Error: Number of courses must be between 1 and {len(courses)}.")
                    continue
                
                print("\nEnter the course numbers (1-5) separated by spaces:")
                course_choices = list(map(int, input().split()))
                
                for choice in course_choices:
                    if 1 <= choice <= len(courses):
                        enrolled_courses.append(courses[choice-1])
                    else:
                        print(f"Invalid course number {choice}. Skipping.")
                
                # Add student to the list
                students.append({
                    "name": name,
                    "roll_number": roll_number,
                    "courses": enrolled_courses
                })
                
                print(f"\nStudent {name} (Roll No: {roll_number}) enrolled successfully!")
                
            except ValueError:
                print("Error: Please enter valid numbers.")
            
        elif choice == '2':
            # View all students
            if not students:
                print("\nNo students enrolled yet.")
            else:
                print("\n===== Enrolled Students =====")
                for i, student in enumerate(students):
                    print(f"\n{i+1}. Name: {student['name']}")
                    print(f"   Roll Number: {student['roll_number']}")
                    print(f"   Enrolled Courses: {', '.join(student['courses'])}")
            
        elif choice == '3':
            # View enrollments by course
            if not students:
                print("\nNo students enrolled yet.")
            else:
                print("\n===== Enrollments by Course =====")
                for course in courses:
                    enrolled_students = [s["name"] for s in students if course in s["courses"]]
                    print(f"\n{course}:")
                    if enrolled_students:
                        for i, student in enumerate(enrolled_students):
                            print(f"   {i+1}. {student}")
                    else:
                        print("   No students enrolled in this course.")
            
        elif choice == '4':
            # Remove a student
            if not students:
                print("\nNo students enrolled yet.")
            else:
                print("\n===== Enrolled Students =====")
                for i, student in enumerate(students):
                    print(f"{i+1}. {student['name']} (Roll No: {student['roll_number']})")
                
                try:
                    student_num = int(input("\nEnter the number of the student to remove: "))
                    if 1 <= student_num <= len(students):
                        removed_student = students.pop(student_num-1)
                        print(f"\nStudent {removed_student['name']} (Roll No: {removed_student['roll_number']}) removed successfully!")
                    else:
                        print("Invalid student number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
        elif choice == '5':
            # Exit the program
            print("\nThank you for using the Student Enrollment Manager!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

# Call the function to run this experiment
print("\nEXPERIMENT 7: STUDENT ENROLLMENT MANAGER")
student_enrollment_manager()
print("\n" + "="*50 + "\n")


############################################################
# 8. Student Record Keeper
############################################################

def student_record_keeper():
    """
    A program to maintain student records with marks and grades.
    """
    print("===== Student Record Keeper =====")
    
    # Initialize data structure for student records
    student_records = []
    
    # Function to calculate grade based on marks
    def calculate_grade(marks):
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B+"
        elif marks >= 60:
            return "B"
        elif marks >= 50:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"
    
    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Add a new student record")
        print("2. View all student records")
        print("3. Search for a student")
        print("4. Update a student's marks")
        print("5. Delete a student record")
        print("6. Exit")
        
        # Get user's choice
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            # Add a new student record
            name = input("\nEnter student name: ")
            roll_number = input("Enter roll number: ")
            
            # Check if roll number already exists
            existing_roll_numbers = [s["roll_number"] for s in student_records]
            if roll_number in existing_roll_numbers:
                print(f"Error: Roll number {roll_number} already exists. Please use a different roll number.")
                continue
            
            try:
                # Get marks for different subjects
                physics = float(input("Enter marks in Physics (out of 100): "))
                chemistry = float(input("Enter marks in Chemistry (out of 100): "))
                mathematics = float(input("Enter marks in Mathematics (out of 100): "))
                
                # Validate marks
                if not (0 <= physics <= 100 and 0 <= chemistry <= 100 and 0 <= mathematics <= 100):
                    print("Error: Marks should be between 0 and 100.")
                    continue
                
                # Calculate total and percentage
                total_marks = physics + chemistry + mathematics
                percentage = total_marks / 3
                
                # Calculate grade
                grade = calculate_grade(percentage)
                
                # Add student record
                student_records.append({
                    "name": name,
                    "roll_number": roll_number,
                    "physics": physics,
                    "chemistry": chemistry,
                    "mathematics": mathematics,
                    "total_marks": total_marks,
                    "percentage": percentage,
                    "grade": grade
                })
                
                print(f"\nStudent record for {name} (Roll No: {roll_number}) added successfully!")
                
            except ValueError:
                print("Error: Please enter valid marks (numbers).")
            
        elif choice == '2':
            # View all student records
            if not student_records:
                print("\nNo student records found.")
            else:
                print("\n===== Student Records =====")
                print(f"{'Name':<20} {'Roll No':<10} {'Physics':<10} {'Chemistry':<10} {'Maths':<10} {'Total':<10} {'Percentage':<10} {'Grade':<5}")
                print("-" * 85)
                for student in student_records:
                    print(f"{student['name']:<20} {student['roll_number']:<10} {student['physics']:<10.1f} "
                          f"{student['chemistry']:<10.1f} {student['mathematics']:<10.1f} {student['total_marks']:<10.1f} "
                          f"{student['percentage']:<10.2f} {student['grade']:<5}")
            
        elif choice == '3':
            # Search for a student
            if not student_records:
                print("\nNo student records found.")
            else:
                search_term = input("\nEnter student name or roll number to search: ")
                found = False
                
                for student in student_records:
                    if search_term.lower() in student['name'].lower() or search_term == student['roll_number']:
                        print("\n===== Student Record Found =====")
                        print(f"Name: {student['name']}")
                        print(f"Roll Number: {student['roll_number']}")
                        print(f"Physics: {student['physics']}")
                        print(f"Chemistry: {student['chemistry']}")
                        print(f"Mathematics: {student['mathematics']}")
                        print(f"Total Marks: {student['total_marks']}")
                        print(f"Percentage: {student['percentage']:.2f}%")
                        print(f"Grade: {student['grade']}")
                        found = True
                
                if not found:
                    print(f"No record found for '{search_term}'.")
            
        elif choice == '4':
            # Update a student's marks
            if not student_records:
                print("\nNo student records found.")
            else:
                roll_number = input("\nEnter the roll number of the student to update: ")
                found = False
                
                for i, student in enumerate(student_records):
                    if student['roll_number'] == roll_number:
                        print(f"\nCurrent marks for {student['name']}:")
                        print(f"Physics: {student['physics']}")
                        print(f"Chemistry: {student['chemistry']}")
                        print(f"Mathematics: {student['mathematics']}")
                        
                        try:
                            # Get new marks
                            physics = float(input("\nEnter new marks in Physics (out of 100): "))
                            chemistry = float(input("Enter new marks in Chemistry (out of 100): "))
                            mathematics = float(input("Enter new marks in Mathematics (out of 100): "))
                            
                            # Validate marks
                            if not (0 <= physics <= 100 and 0 <= chemistry <= 100 and 0 <= mathematics <= 100):
                                print("Error: Marks should be between 0 and 100.")
                                continue
                            
                            # Update marks and recalculate
                            student_records[i]['physics'] = physics
                            student_records[i]['chemistry'] = chemistry
                            student_records[i]['mathematics'] = mathematics
                            student_records[i]['total_marks'] = physics + chemistry + mathematics
                            student_records[i]['percentage'] = student_records[i]['total_marks'] / 3
                            student_records[i]['grade'] = calculate_grade(student_records[i]['percentage'])
                            
                            print(f"\nMarks updated successfully for {student['name']}!")
                            
                        except ValueError:
                            print("Error: Please enter valid marks (numbers).")
                        
                        found = True
                        break
                
                if not found:
                    print(f"No record found for roll number '{roll_number}'.")
            
        elif choice == '5':
            # Delete a student record
            if not student_records:
                print("\nNo student records found.")
            else:
                roll_number = input("\nEnter the roll number of the student to delete: ")
                found = False
                
                for i, student in enumerate(student_records):
                    if student['roll_number'] == roll_number:
                        name = student['name']
                        student_records.pop(i)
                        print(f"\nRecord for {name} (Roll No: {roll_number}) deleted successfully!")
                        found = True
                        break
                
                if not found:
                    print(f"No record found for roll number '{roll_number}'.")
            
        elif choice == '6':
            # Exit the program
            print("\nThank you for using the Student Record Keeper!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

# Call the function to run this experiment
print("\nEXPERIMENT 8: STUDENT RECORD KEEPER")
student_record_keeper()
print("\n" + "="*50 + "\n")


############################################################
# 9. Number Identifier
############################################################

def number_identifier():
    """
    A program to identify properties of a given number.
    """
    print("===== Number Identifier =====")
    print("\nThis program identifies various properties of a given number.")
    
    while True:
        # Get number input from user
        number_input = input("\nEnter a number (or 'exit' to quit): ")
        
        if number_input.lower() == 'exit':
            break
        
        try:
            # Convert input to appropriate number type
            if '.' in number_input:
                number = float(number_input)
                number_type = "Float"
            else:
                number = int(number_input)
                number_type = "Integer"
            
            # Identify number properties
            properties = []
            
            # Check if number is positive, negative, or zero
            if number > 0:
                properties.append("Positive")
            elif number < 0:
                properties.append("Negative")
            else:
                properties.append("Zero")
            
            # For integers, check additional properties
            if number_type == "Integer":
                # Check if even or odd
                if number % 2 == 0:
                    properties.append("Even")
                else:
                    properties.append("Odd")
                
                # Check if prime (for positive numbers)
                if number > 1:
                    is_prime = True
                    for i in range(2, int(number**0.5) + 1):
                        if number % i == 0:
                            is_prime = False
                            break
                    if is_prime:
                        properties.append("Prime")
                
                # Check if perfect square
                if number >= 0 and int(number**0.5)**2 == number:
                    properties.append("Perfect Square")
                
                # Check if perfect cube
                if int(round(number**(1/3)))**3 == number:
                    properties.append("Perfect Cube")
                
                # Check if palindrome
                if str(abs(number)) == str(abs(number))[::-1]:
                    properties.append("Palindrome")
                
                # Check if armstrong number
                digits = str(abs(number))
                digit_sum = sum(int(digit)**len(digits) for digit in digits)
                if digit_sum == abs(number):
                    properties.append("Armstrong Number")
            
            # For floats, check decimal places
            else:
                decimal_part = str(abs(number)).split('.')[-1]
                properties.append(f"Has {len(decimal_part)} decimal places")
            
            # Display results
            print(f"\nNumber: {number}")
            print(f"Type: {number_type}")
            print("Properties:", ", ".join(properties))
            
        except ValueError:
            print("Error: Please enter a valid number.")
    
    print("\nThank you for using the Number Identifier!")

# Call the function to run this experiment
print("\nEXPERIMENT 9: NUMBER IDENTIFIER")
number_identifier()
print("\n" + "="*50 + "\n")
