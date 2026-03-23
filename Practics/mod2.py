N = int(input("Введите N: "))
numbers = list(range(N, N**2))
sqrt_numbers = [round(x**0.5, 2) for x in numbers]
print("Список чисел:", numbers)
print("Квадратные корни:", sqrt_numbers)