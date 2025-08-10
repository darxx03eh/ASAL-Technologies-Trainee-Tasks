with open("../read-write-to-file/information.txt", 'a') as information:
    information.write("\nI like playing basketball, volleyball, and handball as well.")
with open("../read-write-to-file/information.txt", 'r') as information:
    content = information.read()
    print("file content: ")
    print(content)