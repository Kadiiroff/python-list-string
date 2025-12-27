def convert(number: int) -> str:
    return "-".join(str(number))

num = int(input("Enter number: "))
print(f'"{convert(num)}"')

