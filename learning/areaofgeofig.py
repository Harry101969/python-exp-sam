shape = input("Enter the shape(cirle/reactange/triangle): ").lower()
# the .lower() is a method to make uppercase letters to lowercase
area=0
if shape=="cicle":
    radius=float(input("Enter the radius of circle: "))
    area=(3.14 * radius * radius)
elif shape=="rectangle":
    length = float(input("Enter the length: "))
    breadth=float(input("Enter the breadth: "))
    area=(length*breadth)
elif shape=="triangle":
    leng=float(input("Enter length: "))
    height=float(input("Enter height of traingle: "))
    area= 0.5 * leng * height
else:
    print("Wrong shape selected!")