myNumbers = [int(i) for i in input().split()]
numbersLen = len(myNumbers)

if numbersLen == 1:
    print(myNumbers[0])
else:
    for i in range(numbersLen):
        print(myNumbers[i - 1] + myNumbers[(i + 1) % numbersLen], end=' ')
