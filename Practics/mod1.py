N = int(input("Введите количество имен: "))
names = [input("Введите имя: ") for _ in range(N)]
uni = []
for name in names:
    if len(name) not in [len(u) for u in uni]:
        uni.append(name)
print("Исходный список:", names)
print("Список имен разной длины:", uni)