def calculate(number, base):
    symbols = "0123456789ABCDEF"

    result = ""

    if(number == 0):
            return 0
    while(number > 0):
        result = symbols[number % base] + result
        number //= base
    return result

numberStr = input()
if numberStr.isdigit():
    number = int(numberStr)
    binary = calculate(number, 2)
    octal = calculate(number, 8)
    hexadecimal = calculate(number, 16)
    print(f"Двоичная: {binary}, восьмиричная:{octal}, шестандцатиричная: {hexadecimal}")
else:
    print("Не верный ввод")