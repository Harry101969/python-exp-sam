def factorial(n):
    result = 1
    for i in range(2, n+1):
        print(i)
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
