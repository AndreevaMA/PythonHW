
def catalog_update(data):

    if isinstance(data, tuple):
        if len(data) == 5:
            with open(r'C:\Users\maria\Desktop\Python\HW\PythonHW7\phonenum_catalog.csv', 'a', encoding = 'UTF-8') as file:
                file.write(f'Фамилия: {data[0]}; Имя: {data[1]}; Телефон: {data[2]}; Компания: {data[3]}; Должность: {data[4]}; \n')
        else:
            with open(r'C:\Users\maria\Desktop\Python\HW\PythonHW7\phonenum_catalog.csv', 'a', encoding = 'UTF-8') as file:
                file.write(f'Фамилия: {data[0]}; Имя: {data[1]}; Телефон: {data[2]}; \n')


    else:
        with open(r'C:\Users\maria\Desktop\Python\HW\PythonHW7\phonenum_catalog.csv', 'a', encoding = 'UTF-8') as file:
            for element in data:
                if len(element) == 5:
                    file.write(f'Фамилия: {element[0]}; Имя: {element[1]}; Телефон: {element[2]}; Компания: {element[3]}; Должность: {element[4]}; \n')
                if len(element) == 3:
                    file.write(f'Фамилия: {element[0]}; Имя: {element[1]}; Телефон: {element[2]};\n')
