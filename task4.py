a = int(input('Введите число для преобразования: '))
b = ''

while a > 0:
    b += str(a % 8)
    a = a // 8

print(b[::-1])