from functools import reduce

my_list_numbers = list(el for el in range(100, 1001) if el % 2 == 0)
print(my_list_numbers)

print(reduce(lambda prev_el, el: prev_el * el, my_list_numbers))
