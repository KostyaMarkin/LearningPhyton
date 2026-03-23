nums_str = input("Введите числа через пробел: ")
K = int(input("Введите K: "))
numbers = list(map(int, nums_str.split()))
multiples = [x for x in numbers if x % K == 0]
print("Числа, кратные K:", multiples)