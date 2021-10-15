my_dict = {}
with open('my_file2', 'r', encoding='utf-8') as f:
    count_line = 0
    for line in f:
        count_line += 1
        count_words = len(line.split())
        my_dict.update({count_line: count_words})

print(my_dict)
