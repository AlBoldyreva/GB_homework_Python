class MyZeroDivErr(Exception):
    pass


num = int(input('Введите числитель'))
den = int(input('Введите знаменатель'))

try:
    if den == 0:
        raise MyZeroDivErr('Деление на  0!')
except (ZeroDivisionError, MyZeroDivErr) as err:
    print(err)
else:
    print(num / den)
finally:
    print('The end')
