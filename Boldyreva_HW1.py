# 1
name = input('Введите ваше имя')
age = int(input('Введите ваш возраст'))
if age >= 18:
    print('Привет,', name, ', добро пожаловать!')
else: print ('Тем, кому {} лет доступ запрещен'.format(age))

# 2
time_sec = int(input('Введите время в секундах'))
hour = time_sec//3600
min = time_sec%3600//60
sec = time_sec%3600%60
print ('{}:{}:{}'.format(hour, min, sec))

# 3
a = input('Введите число')
b = a + a
c = a + a + a
print(int(a) + int(b) + int(c))

# 4
a = int(input('Введите целое положительное число'))
max_number = 0
while a//10 != 0:
   if a % 10 >= max_number:
       max_number = a % 10
   a = a//10
print(f'Наибольшая цифра равна {max_number}')

# 5
gain = float(input('Введите выручку (млн)'))
cost = float(input('Введите издержки (млн)'))
if gain > cost:
  n = int(input('Введите количество сотрудников'))
   profit = (gain - cost) / gain
   profit_pers = (gain - cost) / n
   print('Прибыль, рентабельность выручки: {:.2f}'.format(profit))
   print('Прибыль в расчете на одного сотрудника {:.2f} млн'.format(profit_pers))
else: print('Фирма отработала в убыток')

# 6
a = int(input('Введите число км спортсмена в 1 день пробежек'))
b = int(input('Введите число км спортсмена в n-ый день пробежек'))
n_day = 1
while a < b:
    a = a * 1.1
    n_day = n_day + 1
print(f'На {n_day}-й день пробежек спортсмен достиг результата - не менее {b} км ')
