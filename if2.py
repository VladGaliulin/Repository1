n = int(input('Введите год '))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('Високосный')
else:
    print('Не високосный')