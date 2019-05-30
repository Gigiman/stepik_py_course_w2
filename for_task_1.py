a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = '\t'

for i in range(c, d+1):
    result += str(i) + '\t'

result += '\n'

for i in range(a, b+1):
    result += str(i) + '\t'

    for j in range(c, d+1):
        result += str(i*j) + '\t'
    result += '\n'

print(result)
