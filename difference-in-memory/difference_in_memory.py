my_list = [10, 20, 30, 40, 50]
addresses = [id(item) for item in my_list]
print(f"Memory addresses: {addresses}")
difference = [addresses[index + 1] - addresses[index] for index in range(len(addresses) - 1)]
print(f"Differences between addresses: {difference}")