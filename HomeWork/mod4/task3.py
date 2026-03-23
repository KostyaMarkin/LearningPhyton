def SearchNOD(numberA, numberB, NOD):
    if(numberA == numberB):
        return numberA
    if(numberB > numberA):
        SearchNOD(numberB, numberA, NOD)
    if(numberA % numberB == 0):
        return NOD
    else:
        NOD = numberA % numberB
        return SearchNOD(numberB, NOD, NOD)

stroka = input().split(' ')
print(f'НОД для чисел {stroka[0]} и {stroka[1]} равен {SearchNOD(int(stroka[0]), int(stroka[1]), 0)}')