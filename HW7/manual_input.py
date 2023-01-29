import csv_read as read


def user_input():

    while True:

        name = input('Фамилия: ')
        second_name = input('Имя: ')

        check_it = read.double_searching(name, second_name)
        if check_it == 0:
            break
        else:
            print('Кажется, такой контакт уже есть! Повтори ввод. :)')

    phone = input('Телефон: ')
    phone = phone.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')

    print('Добавим место работы?', end = ' ')
    while(True):
        answer = input('Выбери "да" или "нет": ')
        if answer not in 'да' and answer not in 'нет':
            print('Извини, я не понимаю. :)')
        else:
            break

    company = None
    job = None
    if answer == 'да':
        company = input('Компания: ')
        job = input('Должность: ')
        new_data = (name, second_name, phone, company, job)
    else:
        new_data = (name, second_name, phone)
    
    return new_data