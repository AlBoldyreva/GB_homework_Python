def int_func(word):
    word = input('Введите строку маленькими латинскими буквами')
    if not word.isascii() or not word.isalpha() or not word.islower():
        print('Ошибка! только маленькие латинские буквы')
        return
    else:
        title_word = word[0].upper + word[1:].lower
        return title_word

print(int_func(input()))

