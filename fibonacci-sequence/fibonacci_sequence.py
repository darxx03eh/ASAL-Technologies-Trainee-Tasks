def fibonacci_sequence(count: int):
    if count <= 0:
        return None, None
    if count == 1:
        return [0], 0
    if count == 2:
        return [0, 1], 1
    fibonacci_list = [0, 1]
    for index in range(2, count):
        fibonacci_list.append(fibonacci_list[index - 2] + fibonacci_list[index - 1])
    return fibonacci_list, fibonacci_list[len(fibonacci_list) - 1]
try:
    count = int(input("Enter the number of numbers you want in the sequence: "))
    fibonacci_list, last_element = fibonacci_sequence(count)
    print(f"fibonacci sequence: {fibonacci_list}, and the last element: {last_element}")
except ValueError as error:
    print("this is not an integer")