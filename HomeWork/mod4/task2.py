def Exponentiation(number, degree, step):
    if(degree == 0):
        return 1
    if(degree == step):
        return number
    else:
        return number * Exponentiation(number, degree - 1, step)

stroka = input().split(' ')
print(f'число {stroka[0]} в степени {stroka[1]} равняется {Exponentiation(int(stroka[0]), int(stroka[1]), 1)}')