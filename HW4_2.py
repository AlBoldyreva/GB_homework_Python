my_list5 = [1, 2, 24, 5, 25, 5, 6, 7]
new_list1 = [my_list5[el] for el in range(1, len(my_list5)) if my_list5[el] > my_list5[el - 1]]
print(new_list1)
