import string
original_text = "Wow! Are you serious? That's amazing; I can't believe it... Really?!"
text_without_punctuatuins = ""
for char in original_text:
    if char not in string.punctuation:
        text_without_punctuatuins += char
print(f"original text: {original_text}")
print(f"new text: {text_without_punctuatuins}")