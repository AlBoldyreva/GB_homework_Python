def my_func_pow(a, b):
    try:
        a = float(a)
        b = int(b)
    except ValueError:
        print('Ошибка! Введите действительное а и целое b')
        return
    if a <= 0 or b >= 0:
        print('Ошибка! Введите положительное а и отрицательное b')
        return
    pow_res = a ** b
    return pow_res


a = input('Введите действительное положительное число')
b = input('Введите целое отрицательное число')
print(round((my_func_pow(a, b)), 4))


def my_func_pow2(c, d, i=1):
    try:
        c = float(c)
        d = int(d)
    except ValueError:
        print('Ошибка! Введите действительное c и целое d')
        return
    if c <= 0 or d >= 0:
        print('Ошибка! Введите положительное c и отрицательное d')
        return
    pow_res2 = 1
    while i <= abs(d):
        pow_res2 /= c
        i += 1
    return pow_res2

c = input('Введите действительное положительное число')
d = input('Введите целое отрицательное число')
print(round((my_func_pow2(c, d)), 4))
