number = input("Enter a numbers: ")
countZeros = 0
countOnes = 0
for char in number:
    if char == '0':
        countZeros += 1
    if char == '1':
        countOnes += 1
if countZeros == countOnes:
    print("yes")
else:
    print("no")