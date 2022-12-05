a = int(input('Введите число для преобразования: '))
b = ''

while a > 0:
    b += str(a % 2)
    a = a // 2

print(b[::-1])