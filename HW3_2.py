def person_data(name, surname, birth, city, email, tel):
    print(name, surname, birth, city, email, tel)
person_data(name=input('Введите имя'),
            surname=input('Введите фамилию'),
            birth=input('Введите год рождения'),
            city=input('Введите город'),
            email=input('Введите почту'),
            tel=input('Введите телефон'))
