myNumbers = [int(i) for i in input().split()]
myNumbers.sort()
repeatingNumbs = []

for i in myNumbers:
    if myNumbers.count(i) > 1:
        if i not in repeatingNumbs:
            repeatingNumbs.append(i)
            print(i)
