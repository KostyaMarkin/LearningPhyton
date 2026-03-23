def CheckNumbers(numbers, numberForCheck, position, result):
    i = -1
    for number in numbers:
        i += 1
        if position == i:
            continue
        if number == numberForCheck:
            result[1] = True
        else:
            result[2] = True

    if i != position:
       return CheckNumbers(stroka, stroka[position + 1], position + 1, result)
    else:
        if result[1] & result[2]:
            return "Есть равные и неравные числа"
        if result[1]:
            return "Все числа равные"
        if result[2]:
            return "Все числа не равные"

stroka = input().split(' ')
result = {1: False, 2: False }
print(CheckNumbers(stroka, stroka[0], 0, result))



