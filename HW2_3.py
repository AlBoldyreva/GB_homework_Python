list_year = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
date = int(input('Введите месяц в виде целого числа от 1 до 12 и я скажу вам какое это время года'))
if list_year.index(date) <= 1:
    print('Это зима')
elif list_year.index(date) > 1 and list_year.index(date) <= 4:
    print('Это весна')
elif list_year.index(date) > 4 and list_year.index(date) <= 7:
    print('Это лето')
elif list_year.index(date) > 7 and list_year.index(date) <= 10:
    print('Это осень')
else:
    print('Это зима')

dict_year = {1: 'Это Зима', 2: 'Это Зима', 12: 'Это Зима', 3: 'Это Весна', 4: 'Это Весна', 5: 'Это Весна',
             6: 'Это Лето', 7: 'Это Лето', 8: 'Это Лето', 9: 'Это Осень', 10: 'Это Осень', 11: 'Это Осень'}
date = int(input('Введите месяц в виде целого числа от 1 до 12 и я скажу вам какое это время года'))
print(dict_year[date])
