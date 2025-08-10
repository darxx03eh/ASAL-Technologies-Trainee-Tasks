import random
duplicate_list = [random.randint(1, 10) for _ in range(20)]
print(f"before removing duplicate: {duplicate_list}")
without_duplicate = list(set(duplicate_list))
print(f"after removing duplicate: {without_duplicate}")