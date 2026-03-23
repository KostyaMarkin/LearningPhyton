line = input()

firstSpace = line.find(" ")
secondSpace = line.find(" ", firstSpace + 1)

numberAStr = line[:firstSpace]
numberBStr = line[firstSpace + 1:secondSpace]
numberCStr = line[secondSpace + 1:]

numberA = int(numberAStr)
numberB = int(numberBStr)
numberC= int(numberCStr)

if numberA >= numberB and numberA >= numberC:
    max_num = numberA
elif numberB >= numberA and numberB >= numberC:
    max_num = numberB
else:
    max_num = numberC

if numberA <= numberB and numberA <= numberA:
    min_num = numberA
elif numberB <= numberA and numberB <= numberC:
    min_num = numberB
else:
    min_num = numberC

middle = numberA + numberB + numberC - max_num - min_num

print(middle)