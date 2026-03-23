str = input()
size = str.find(',')
symbolInput = str[size+1]
result = 0
firstPoint = -1
secondPoint = -1
for n in range(size-1):
    if(firstPoint > -1 and str[n] == symbolInput):
        secondPoint = n
    elif(firstPoint > -1):
        break
    elif (str[n] == symbolInput):
        firstPoint = n
        secondPoint = n
    else:
        continue

resultStr = str[firstPoint:secondPoint+1]
for char in resultStr:
    result += 1
print(result)