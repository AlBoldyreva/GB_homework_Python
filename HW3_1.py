def divide_func(var_1, var_2):
    try:
        div = var_1 / var_2
    except ZeroDivisionError:
        print('Ошибка! Деление на 0')
    return div


var_1 = int(input('Введите первое число'))
var_2 = int(input('Введите второе число'))
print(divide_func(var_1, var_2))
