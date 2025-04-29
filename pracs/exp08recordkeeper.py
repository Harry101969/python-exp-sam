students = []

for i in range(2):
    name=input("Enter the name: ")
    roll=int(input("Enter ur roll no: "))
    branch=input("Enter ur branch: ")
    students.append({
     'Name':name,
     "RollNo":roll,
     "Branch":branch   
    })

print('Students Record')
students.pop()
for s in students: 
    print(f"Name:{s['Name']} , RollNo:{s['RollNo']} , Branch:{s['Branch']}.")
    
    