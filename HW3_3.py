def sum_max(arg_1, arg_2, arg_3, my_list3=[]):
    my_list3.append(arg_1)
    my_list3.append(arg_2)
    my_list3.append(arg_3)
    my_list3.sort(reverse=True)
    summa = my_list3[0] + my_list3[1]
    return summa


print(sum_max(2, 56, 1))
