a = int(input('Введите число для преобразования: '))
b = ''

while a > 0:
    b += str(a % 5)
    a = a // 5

print(b[::-1])