a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))
if c < a:
    print ('Число c меньше а')
elif c == a:
    print ('Число c равно а')
elif c > a and c < b:
    print ('Число с находится в промежутке между а и b')
elif c == b:
    print ('Число c равно b')
else:
    print ('Число c больше b')