sentence = input('Введите слова через пробел')
my_list = sentence.split()
el = 0
for i in my_list:
    while el < len(my_list):
        print(el + 1, my_list[el][0:10])
        el += 1
