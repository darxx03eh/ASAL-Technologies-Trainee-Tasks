first_list = [
    1, 2, 3, 4, 5
]
second_list = [
    6, 7, 8, 9, 10
]
merge_list = [
    *first_list,
    *second_list
]
print(f"before reverse: {merge_list}")
merge_list = merge_list[::-1]
print(f"after reverse: {merge_list}")