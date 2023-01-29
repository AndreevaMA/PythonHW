

def action_choice():
    print()
    print('Выбери, что я должен сделать. :)')
    print('Добавить новый контакт вручную? Нажми 1.')
    print('Загрузить данные по нескольким контактам? Нажми 2.')
    print('Выполнить поиск? Нажми 3.')
    print('Экспортировать данные справочника в html? Нажми 4.')
    print()

    while True:
        my_choice = int(input('Мой выбор: '))
        if str(my_choice) not in '1234':
            print('Кажется, что-то пошло не так. :)')
        else:
            break

    print()
    
    return my_choice