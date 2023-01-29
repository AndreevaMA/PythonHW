

def bulk_read():
    to_upload = input('Какой файл будем загружать? Напиши название: ')

    path = rf'C:\Users\maria\Desktop\Python\HW\PythonHW7\{to_upload}.txt'
    file_data = open(path, 'r', encoding = 'UTF-8')

    new_data = []
    new_contact = []

    for index, line in enumerate(file_data):
        if index == 0:
            first_line = line
            break

    format = 1
    if not first_line.lower().strip().isalpha():
        format = 0
    # print(f'Формат выбранного файла: {format}.')

    if format == 1:
        new_contact.append(first_line.strip())
        for line in file_data:
            if len(line.strip()) != 0:
                new_contact.append(line.strip())
            else:
                new_data.append(new_contact)
                new_contact = []
        new_data.append(new_contact)

    else:
        new_data.append(list(first_line.strip().split(',')))
        for line in file_data:
            new_contact += list(line.strip().split(','))
            new_data.append(new_contact)
            new_contact = []

    file_data.close()

    for element in new_data:
            temp = element[2].replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
            element[2] = temp
            element = tuple(element)
        
    return new_data
    
