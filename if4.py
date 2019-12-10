x1 = int(input('Введите значение x1: '))
y1 = int(input('Введите значение y1: '))
h = int(input('Введите высоту h: '))
w = int(input('Введите ширину w: '))
x2 = int(input('Введите значение x2: '))
y2 = int(input('Введите значение y2: '))
if x2 < x1 and y2 > y1 or x2 > w and y2 > h:
    print('Точка x2y2 находится за пределами плоскости z')
elif x2 == x1 and y1 == y2 and x2 == h and y2 == w:
        print('Точка x2y2 находится на плоскости z')
elif x2 > x1 and y2 < y1 or x2 < w and y2 < h:
    print('Точка x2y2 находится в плоскости z')