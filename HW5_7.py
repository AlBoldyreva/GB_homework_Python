import json
my_dict4 = {}
with open('my_file8', 'r', encoding='utf-8') as f:
    n = 0
    sum_profit = 0
    for line in f:
        a = line.split()
        profit = int(a[-2]) - int(a[-1])
        if profit > 0:
            sum_profit += profit
            n +=1
        my_dict4.update({a[0]: profit})
    my_list4 = [my_dict4, {'average_profit': sum_profit/n}]

with open("my_file.json", "w") as write_f:
    json.dump(my_list4, write_f)