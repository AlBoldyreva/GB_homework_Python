my_list = []
a = []
with open('my_file3', 'r', encoding='utf-8') as f:
    count_line = 0
    sum_salary = 0
    for line in f:
        count_line += 1
        a = line.split()
        if float(a[1]) < 20000:
            my_list.append(a[0])
        sum_salary += float(a[1])
print(my_list)
print(sum_salary / count_line)
