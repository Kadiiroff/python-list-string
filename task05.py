

def split_lines(text: list) -> list:

    return text.replace("|", "\n")
    

text = input("Enter words: ")
print(split_lines(text))


