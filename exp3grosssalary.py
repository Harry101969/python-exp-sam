# Calculates gross salary by adding HRA and DA to basic salary
basic = float(input("Enter basic salary: "))
hra = 0.2 * basic  # 20% HRA-House rent allowance
da = 0.1 * basic   # 10% DA-dearness allowance
gross = basic + hra + da
print("Gross Salary:", gross)
