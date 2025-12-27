
def get_domens(emails: list) -> list:

    email_list = [email.strip() for email in emails.split(',')]

    domains = {email[email.index('@'):] for email in email_list}
    
    return list(domains)

text = input("Enter domens: ")
print(get_domens(text))


