def convert(string: str) -> str:
    return '_'.join(string.lower().replace(",", "").split())

text = input("Enter strings: ")
print(convert(text))
