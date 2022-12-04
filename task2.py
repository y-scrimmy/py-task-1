a = 1
b = input('Введите число n')
c = 0

for i in range(a, int(b) + 1):
    c = c + i**2

print(c)