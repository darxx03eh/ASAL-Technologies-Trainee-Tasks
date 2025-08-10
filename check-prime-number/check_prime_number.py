from math import sqrt
def is_prime(num: int):
    for i in range(2, int(sqrt(num) + 1)):
        if not num%i:
            return False
    return True
try:
    num = int(input("Enter an integer: "))
    print(f"{num} {"is a prime number" if is_prime(num) else "is not a prime number"}")
except ValueError as error :
    print("this is not an integer")