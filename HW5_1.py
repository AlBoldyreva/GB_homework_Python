file = open("my_file1.txt", "w", encoding='UTF-8')
file.write(input('Введите то, что вам надо записать') + '\n')
file = open("my_file1.txt", "a", encoding='UTF-8')
f = False
while not f:
    a = input('Введите то, что вам надо дозаписать')
    if a == '':
        f = True
    else:
        file.write(a + '\n')
