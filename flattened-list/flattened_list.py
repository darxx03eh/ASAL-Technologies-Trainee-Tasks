def flatten_list(nested: list):
    flatten = []
    for item in nested:
        if isinstance(item, list):
            flatten.extend(flatten_list(item))
        else: flatten.append(item)
    return flatten
nested = [1, [2, 3, [4, 5]], 6, [7, 8]]
flat = flatten_list(nested)
print(f"before: {nested}")
print(f"after: {flat}")