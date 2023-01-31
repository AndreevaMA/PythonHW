import choice


def start():
    print('Выберите действие:\n\
        - Добавить ученика (нажмите 1)\n\
        - Найти ученика (нажмите 2)\n\
        - Вывести список учеников (нажмите 3)')
    print()

    value = input('Действие: ').lower()
    print()

    match value:
        case '1':
            choice.chose_adding()
        case '2':
            choice.chose_searching()
        case '3':
            choice.chose_list()