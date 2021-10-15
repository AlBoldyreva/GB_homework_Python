file = open("my_file6.txt", "w", encoding='UTF-8')
file.write(input('Введите числа через пробел'))
with open('my_file6.txt', 'r', encoding='utf-8') as file:
    sum_numbers = 0
    for line in file:
        a = line.split()
        for i in range(len(a)):
            sum_numbers += int(a[i])
            i += 1

print(sum_numbers)
