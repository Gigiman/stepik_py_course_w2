s = 0
multiplied = 0
while True:
    a = int(input())
    s += a
    multiplied += a*a

    if s == 0:
        break

print(multiplied)
