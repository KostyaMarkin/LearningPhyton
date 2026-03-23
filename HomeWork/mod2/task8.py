stroka = input().strip()
words = []
current = ""
for char in stroka:
    if char ==' ':
        if current:
            words.append(current)
            current = ""
    else:
        current += char
if current:
    words.append(current)

result =""
for word in words:
    result += word[-1]
print(result)