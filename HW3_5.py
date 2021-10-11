def my_sum(str1, sum1=0):
    list1 = str1.split()
    for i in range(0, len(list1)):
        if str(list1[i]) != '*':
            sum1 = sum1 + int(list1[i])
            i += 1
        else:
            print(sum1)
            break
    return sum1


a = input('Введите числа через пробел')
print(my_sum(a))