import re


def find_emails(text):
    pattern = r'\b[a-zA-Z0-9+_#-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

    matches = re.findall(pattern, text)

    return matches


# Основная программа
if __name__ == "__main__":

    text = "Jones and Palin met at Oxford University, where they performed together ysinghmanga@206954.com with the Oxford Revue. (6boutheina+14@weammo.xyz)"
    emails = find_emails(text)

    print("Найденные email-адреса:")
    if emails:
        for email in emails:
            print(email)
    else:
        print("Email-адреса не найдены.")