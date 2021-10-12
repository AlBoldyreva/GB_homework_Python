my_list = [1, 2, 4, 5, 5, 6, 7]
new_gen = (el for el in my_list if my_list.count(el) == 1)
print(*new_gen)
