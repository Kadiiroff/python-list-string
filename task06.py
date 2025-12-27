

def check_polindrome(text: list) -> list:
    polindrome = [p for p in text.split() if p == p[::-1]]
    return polindrome

text = input("Enter a text: ")
print(check_polindrome(text))
