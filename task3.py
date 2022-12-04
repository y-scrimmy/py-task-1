a = int(input('Введите число для преобразования: '))
b = ''

while a > 0:
    b += str(a % 3)
    a = a // 3

print(b[::-1])