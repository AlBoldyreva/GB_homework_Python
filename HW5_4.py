my_dict2 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('my_file4', 'r', encoding='utf-8') as f:
    file = open("my_file5.txt", "w", encoding='UTF-8')
    for line in f:
        a = line.split()
        file.write('{} {} {}\n'.format(my_dict2.get(a[0]), a[1], a[2]))

