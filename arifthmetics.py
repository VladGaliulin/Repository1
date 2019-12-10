a = float(input('Введите число а: '))
b = float(input('Введите число b: '))
c = (input('Введите знак: '))
if c == "/":
    print(f'{a / b}')
elif c == "*":
    print(f'{a * b}')
elif c == "+":
    print(f'{a + b}')
elif c == "-":
    print(f'{a - b}')
else:
    print('Некоректный знак')