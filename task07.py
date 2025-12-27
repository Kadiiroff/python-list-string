

text = input("Matn kiriting: ")


text = text.replace(',', '')

parts = text.split()


for part in parts:
    key, value = part.split(':')
    print(f"{key}: {value}")
