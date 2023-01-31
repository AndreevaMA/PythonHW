import view


student_id_counter = 0

students = {}
# format {1: {'Имя': 'Иван', 'Фамилия': 'Иванов', 'Дата_рождения': '2000-01-01'}}

classes = {}
# format {'1a': [],'1b': []}



#----------------------Методы для внесения в базу данных информации о новом ученике-------------------

# добавление в базу нового ученика
def AddNewStudent():
    new_student = dict()
    new_student['Id'] = GetNewId() # ключ для словаря
    new_student['Имя'] = view.InputInfo('имя ученика')
    new_student['Фамилия'] = view.InputInfo('фамилию ученика')
    new_student['Дата_рождения'] = view.InputInfo('дату рождения ученика')
    AddStudentsInClasses(new_student['Id'])
    return new_student      # {Id: , Имя: , Фамилия: , Дата_рождения: }


# определение ID последнего в базе ученика и назначение ID для нового ученика
def GetNewId():
    global student_id_counter
    student_id_counter += 1
    return student_id_counter


# добавление ученика в существующий или новый класс
def AddStudentsInClasses(student_id):
    global classes
    student_class = view.InputInfo('номер класса ученика')
    if student_class in classes:
        classes[student_class].append(student_id)
    else:
        classes[student_class] = [student_id]


# обновление базы учеников в отдельном csv файле
def SaveStudents(student):
    with open(r'C:\Users\maria\Desktop\Python\S\PythonS8\students.csv', 'a', encoding = 'UTF-8') as file:
        file.write(f"{student['Id']};{student['Имя']};{student['Фамилия']};{student['Дата_рождения']}\n")




#---------------------Работа с файлом, в котором хранится ID последнего в базе ученика-----------------

# обращение к файлу и считывание ID
def GetLastStudentId():
    global student_id_counter
    with open(r'C:\Users\maria\Desktop\Python\S\PythonS8\last_student_id.txt', 'r', encoding = 'UTF-8') as file:
        student_id_counter = int(file.read())

# обновление ID
def SaveLastStudentId():
    global student_id_counter
    with open(r'C:\Users\maria\Desktop\Python\S\PythonS8\last_student_id.txt', 'w', encoding = 'UTF-8') as file:
        file.write(str(student_id_counter))




#-------------------------Работа с файлом, в котором хранится информация о классах---------------------

# обновление базы классов в отдельном txt файле
def SaveClasses():
    global classes
    with open(r'C:\Users\maria\Desktop\Python\S\PythonS8\classes.txt', 'w',  encoding = 'UTF-8') as file:
        for key, value in classes.items():
            file.write(f'{key} - {value}\n')


# обращение к файлу и считывание информации о классах
def GetClasses():
    with open(r'C:\Users\maria\Desktop\Python\S\PythonS8\classes.txt', 'r',  encoding = 'UTF-8') as file:
        temp = file.readlines()
        global classes
        classes = {}
        for element in temp:
            classes[element[:element.index(' ')]] = list(map(int, element[element.index('[') + 1:-2].split(', ')))
        return classes




#---------------------------Методы для поиска информации о конкретном ученике--------------------------

# поиск класса, в котором учится ученик
def GetHisClass(data):
    current_classes = GetClasses()
    for item in current_classes.values():
        flag = 0
        if int(data[0]) in item:
            my_index = list(current_classes.values()).index(item)
            flag = 1
            break
    classes_list = list(current_classes.keys())
    if flag:
        return classes_list[my_index]


# обращение к файлу и считывание информации об ученике по имени и фамилии
def GetStudent(data):
    with open(r'C:\Users\maria\Desktop\Python\S\PythonS8\students.csv', 'r',  encoding = 'UTF-8') as file:
        temp = file.readlines()
        result1 = 0
        for element in temp:
            student = element.strip().split(';')
            if student[1] == data[0] and student[2] == data[1]:
                result1 = student
                break
        if result1 == 0:
            print('Такой ученик не найден.')
            result2 = 0
        else:
            result2 = GetHisClass(result1)
    return (result1, result2)


# обращение к файлу и считывание информации об ученике по его ID
def GetStudentByID(data):
    with open(r'C:\Users\maria\Desktop\Python\S\PythonS8\students.csv', 'r',  encoding = 'UTF-8') as file:
        temp = file.readlines()
        result = 0
        for element in temp:
            student = element.strip().split(';')
            if student[0] == str(data):
                result = student
                break
        if result == 0:
            print('Такой ученик не найден.')
    return result




#-----------------------------------Вывод сгруппированной информации----------------------------------

# вывод списка всех учеников класса
def ShowClassTotal(data):
    classes_info = GetClasses()
    if data not in classes_info:
        print(f'Класс {data} отсутствует в списке классов школы.')
    else:
        to_show = classes_info[data] # [1, 3, 5]
        print(f'Список учеников {data} класса:')
        for student_id in to_show:
            student_info = GetStudentByID(student_id)
            print(f'{student_info[1]} {student_info[2]}')

