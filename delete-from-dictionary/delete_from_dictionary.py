my_dict = {
    "name":"mahmoud darawsheh",
    "age": 22,
    "department": "CSE"
}

removed_value = my_dict.pop("age", None)
if removed_value is not None:
    print("removed successfully, the value is {}".format(removed_value))
else: print("key not found")
print(f"dictionary after delete the key {my_dict}")