first_dict = {
    'Mahmoud Darawsheh': 22,
    'Hussam Burqan': 22
}
second_dict = {
    'Abdullah Noor': 21,
    'Mustafa Faris': 22
}
merge_dict = {
    **first_dict,
    **second_dict
}
print(merge_dict)