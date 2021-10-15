my_dict3 = {}
with open('my_file7', 'r', encoding='utf-8') as f:
    for line in f:
        sum_hours = 0
        a = line.split()
        name_lesson = a[0][:-1]
        for i in range(1, len(a)):
            if a[i] != '—':
                b = int(a[i][:a[i].index('(')])
                sum_hours += b
            else:
                continue
        my_dict3.update({name_lesson: sum_hours})

print(my_dict3)
