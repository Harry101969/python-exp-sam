# Calculates gross salary by adding HRA and DA to basic salary
name = input("Enter the name of the employee: ")
basic = float(input("Enter basic salary: "))
ta = 0.3*basic  # 30% travel-allowance
hra = 0.2 * basic  # 20% HRA-House rent allowance
da = 0.1 * basic   # 10% DA-dearness allowance
gross = basic + hra + da + ta
print(f"Gross salary of {name}: ", gross)
