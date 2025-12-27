def get_info(fish: str) -> str:
    name, surname, patronymic = fish.split()
    return f"{surname} {name} {patronymic}"
text = input("Enter FIO: ")
print(get_info(text))