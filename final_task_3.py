numArr = [int(i) for i in input().split()]
n = int(input())
if n not in numArr:
    print("Отсутствует")
else:
    [print(i, end=" ") for i, x in enumerate(numArr) if x == n]
#x in enumaerates разобрать подробнее в курсе не встречалось, cheers to stackoverflow