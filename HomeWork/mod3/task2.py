n=input()
print(bin(int(n))[2:], oct(int(n))[2:], hex(int(n))[2:] if n.isdigit() and int(n)>0 else "Неверный ввод")