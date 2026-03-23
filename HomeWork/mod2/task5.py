domain = input()
parts = []
current = ""

for char in domain:
    if(char =="."):
        parts.append(current)
        current = ""
    else:
        current += char
parts.append(current)

for i in range(len(parts)-1, -1, -1):
    print(parts[i])