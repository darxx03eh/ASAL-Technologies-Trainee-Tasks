def find_factorial(num: int):
    factorial = 1
    for i in range(1, num + 1):
        factorial *=i
    return factorial
try:
    num = int(input("Enter an integer: "))
    print(f"factorial for {num} is: {find_factorial(num)}")
except ValueError as error:
    print("this is not an integer")