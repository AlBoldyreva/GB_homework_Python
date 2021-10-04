my_list1 = [8, 7, 6, 5, 4, 4, 3, 2]
number = int(input('Введите число'))
count = 0
for i in my_list1:
    if number <= i:
        count += 1
my_list1.insert(count, number)
print(my_list1)
