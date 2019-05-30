a = int(input())
b = int(input())
NOK = 1

while NOK % a != 0 or NOK % b != 0:
    NOK += 1
print(NOK)
