prices_str = input("Введите цены через пробел: ")
K = int(input("Введите K: "))
M = int(input("Введите M: "))
prices = list(map(int, prices_str.split()))
discount = [price - (price // K) * M for price in prices]
print("Цены до скидки:", prices)
print("Цены после скидки:", discount)