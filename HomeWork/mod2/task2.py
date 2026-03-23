from math import sqrt

numberA = int(input('Введите сторону A '))
numberB = int(input('Введите сторону B '))
print("Периметр приямоугольника:" + str(numberA + numberB))
print("Площадь приямоугольника:" + str(numberA * numberB))
print(f"Диагональ прямоугольника:  {sqrt(numberA ** 2 + numberB** 2):.2f}")