# ===== List Example =====
my_list = [1, 2, 3]

# + operator → concatenation
new_list = my_list + [4, 5]
print("List after +:", new_list)

# * operator → repetition
repeated_list = my_list * 2
print("List after *:", repeated_list)

# in operator → membership test
print("Is 2 in my_list?", 2 in my_list)


# ===== Tuple Example =====
my_tuple = (10, 20, 30)

# + operator → concatenation
new_tuple = my_tuple + (40, 50)
print("Tuple after +:", new_tuple)

# * operator → repetition
repeated_tuple = my_tuple * 3
print("Tuple after *:", repeated_tuple)

# in operator → membership test
print("Is 25 in my_tuple?", 25 in my_tuple)


# ===== Dictionary Example =====
my_dict = {"a": 1, "b": 2}

# in operator → checks if key exists
print("Is 'a' in my_dict?", "a" in my_dict)

# update operator (| in Python 3.9+)
new_dict = my_dict | {"c": 3}
print("Dictionary after |:", new_dict)

# del operator → remove key
del my_dict["b"]
print("Dictionary after del:", my_dict)
