with open("information.txt", 'w') as information:
    information_list = [
        "I am Mahmoud Darawsheh,\n",
        "I am 22 years old,\n", 
        "I study at Palestine Technical University – Kadoorie,\n",
        "Major: Computer Systems Engineering."
    ]
    information.writelines(information_list)
with open("information.txt", 'r') as information:
    content = information.read()
    print("file content: ")
    print(content)