from math import factorial


def fact_gen(number):
    fact_num = 1
    if number == 0:
        yield 1
    for i in range(1, number + 1):
        fact_num *= i
        yield fact_num


for el in fact_gen(int(input('Введите число'))):
    print(el)
