# Original list
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# Using del: deletes element by index (no return value)
del my_list[1]  # deletes the element at index 1 (20)
print("After del (index 1):", my_list)

# Using remove(): deletes element by value (no return value)
my_list.remove(30)  # removes the first occurrence of 30
print("After remove(30):", my_list)

# Using pop(): deletes element by index and returns it
popped_value = my_list.pop(1)  # removes element at index 1
print("After pop(1):", my_list)
print("Popped value:", popped_value)
