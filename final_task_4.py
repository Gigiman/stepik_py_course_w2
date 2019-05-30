matrix = []
a = input()
while a != 'end':
    matrix.append([int(i) for i in a.split()])
    a = input()
res = ''
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        a = matrix[i - 1][j]
        b = matrix[i][j - 1]
        if j == len(matrix[i]) - 1:
            c = matrix[i][0]
        else:
            c = matrix[i][j + 1]
        if i == len(matrix) - 1:
            d = matrix[0][j]
        else:
            d = matrix[i + 1][j]
        res += str(a + b + c + d) + ' '
    res += '\n'

print(res)
