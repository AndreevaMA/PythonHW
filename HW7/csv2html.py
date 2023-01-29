

def html_create():
    print()
    print('Выбери формат для экспорта: ')
    print('1 - Все данные контакта отдельной строкой, разделитель - пустая строка.')
    print('2 - Все данные контакта одной строкой через запятую.')
    print()

    while True:
        my_choice = int(input('Мой выбор: '))
        if str(my_choice) not in '12':
            print('Кажется, что-то пошло не так. :)')
        else:
            break

    path = r'C:\Users\maria\Desktop\Python\HW\PythonHW7\phonenum_catalog.csv'
    file_data = open(path, 'r', encoding = 'UTF-8')

    if my_choice == 1:
        style = 'style="font-size:14px;"'
        html = '<html>\n  <head></head>\n  <body>\n'

        for line in file_data:
            temp = list(line.strip().split(';'))
            del temp[-1]

            if len(temp) == 5:
                html += '     <p {}>{}</p>\n'.format(style, temp[0].replace("Фамилия: ", ""))
                html += '     <p {}>{}</p>\n'.format(style, temp[1].replace("Имя: ", ""))
                html += '     <p {}>{}</p>\n'.format(style, temp[2].replace("Телефон: ", ""))
                html += '     <p {}>{}</p>\n'.format(style, temp[3].replace("Компания: ", ""))
                html += '     <p {}>{}</p>\n'.format(style, temp[4].replace("Должность: ", ""))
                html += '&nbsp'
            else:
                html += '     <p {}>{}</p>\n'.format(style, temp[0].replace("Фамилия: ", ""))
                html += '     <p {}>{}</p>\n'.format(style, temp[1].replace("Имя: ", ""))
                html += '     <p {}>{}</p>\n'.format(style, temp[2].replace("Телефон: ", ""))
                html += '&nbsp'

        html += '  </body>\n</html>'

        file_data.close()

        with open(r'C:\Users\maria\Desktop\Python\HW\PythonHW7\export_html_format1.html', 'w', encoding = 'UTF-8') as page:
            page.write(html)
        
        return html

    else:
        style = 'style="font-size:14px;"'
        html = '<html>\n  <head></head>\n  <body>\n'

        for line in file_data:
            temp_list = list(line.strip().split(';'))
            del temp_list[-1]
            temp_string = ','.join(temp_list)

            if len(temp_list) == 5:
                html += '     <p {}>{}</p>\n'.format(style, temp_string.replace("Фамилия: ", "")\
                    .replace("Имя: ", "").replace("Телефон: ", "").replace("Компания: ", "").replace("Должность: ", ""))
            else:
                html += '     <p {}>{}</p>\n'.format(style, temp_string.replace("Фамилия: ", "")\
                .   replace("Имя: ", "").replace("Телефон: ", ""))

        html += '  </body>\n</html>'

        file_data.close()

        with open(r'C:\Users\maria\Desktop\Python\HW\PythonHW7\export_html_format2.html', 'w', encoding = 'UTF-8') as page:
            page.write(html)
        
        return html




