my_list1 = list(input('Введите список'))
print(my_list1)
for i in range(0, len(my_list1) - 1, 2):
    my_list1[i], my_list1[i + 1] = my_list1[i + 1], my_list1[i]
print(my_list1)
