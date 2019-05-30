myNum = int(input())
res = []
i = 1

while len(res) < myNum:
    for n in range(1, i + 1):
        res.append(i)
    i += 1
print(*res[:myNum])