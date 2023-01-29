
# поиск телефона сразу по имени и фамилии

def double_searching(data1, data2):
    path = rf'C:\Users\maria\Desktop\Python\HW\PythonHW7\phonenum_catalog.csv'
    file_data = open(path, 'r', encoding = 'UTF-8')

    search_result = 0

    for line in file_data:
        temp = list(line.strip().split(';'))
        if (temp[0].find(data1) != -1 and temp[1].find(data2) != -1)\
            or (temp[1].find(data1) != -1 and temp[0].find(data2) != -1):
            search_result = temp[2].replace('Телефон: ', '')
            break
    
    file_data.close()
    return search_result



# поиск телефона по имени или фамилии

def searching(data):
    path = rf'C:\Users\maria\Desktop\Python\HW\PythonHW7\phonenum_catalog.csv'
    file_data = open(path, 'r', encoding = 'UTF-8')

    search_result_name = []
    search_result_num = []

    for line in file_data:
        temp = list(line.strip().split(';'))
        if temp[0].find(data) != -1 or temp[1].find(data) != -1:
            if temp[0].find(data) != -1:
                search_result_name.append(temp[1].replace('Имя: ', ''))
                search_result_num.append(temp[2].replace('Телефон: ', ''))
            if temp[1].find(data) != -1:
                search_result_name.append(temp[0].replace('Фамилия: ', ''))
                search_result_num.append(temp[2].replace('Телефон: ', ''))

    file_data.close()

    if len(search_result_name) == 0:
        result = 0
    if len(search_result_name) == 1:
        result = search_result_num[0]
    else:
        print('Я нашёл несколько подходящих контактов!')
        print(f'Вот они: {", ".join(search_result_name)}.')
        specify_it = input('Какой из контактов тебе нужен? :) ')
        result = double_searching(data, specify_it)
    
    return result


# выполнение поиска контакта и выдача результата поиска

def find_contact():
    search_it = input('Для поиска введи имя или фамилию контакта: ')
    phonenum = searching(search_it)
    if phonenum == 0:
        print('Контакт не найден.')
    else:
        print(phonenum)
