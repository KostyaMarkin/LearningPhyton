current = "1234567890+"
stroka = input().strip()
result = ""
for char in stroka:
    if current.find(char)>0:
        result += char
print(result)