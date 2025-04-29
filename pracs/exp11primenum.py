def is_prime(n):
    if n <= 1: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

num = int(input("Enter a number: "))
print("Prime" if is_prime(num) else "Not Prime")
