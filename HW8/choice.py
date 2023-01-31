import view
import model


def chose_adding():
    model.GetLastStudentId()
    model.GetClasses()
    stop = False
    while not stop:
        model.SaveStudents(model.AddNewStudent())
        if view.InputInfo('"готово" для завершения').lower() == 'готово':
            stop = True
    model.SaveClasses()
    model.SaveLastStudentId()


def chose_searching():
    to_find = view.InputInfo('имя и фамилию ученика').split()
    x = model.GetStudent(to_find)
    if x[0] != 0 and x[1] != 0:
        print(f'{x[0][1]} {x[0][2]}, дата рождения: {x[0][3]}, учится в {x[1]} классе.')


def chose_list():
    show_list = view.InputInfo('номер класса')
    model.ShowClassTotal(show_list)
