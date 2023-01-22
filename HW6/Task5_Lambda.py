# Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).

#------------------------------------исходный код------------------------------------------

# метод для проверки результата ввода числа с консоли
# def validate_input(string):
#     if string in ('1', '2', '3', '4'):
#         return True
#     else:
#         return False

# values = ['x > 0, y > 0', 'x < 0, y > 0', 'x < 0, y < 0', 'x > 0, y < 0']
# quadrant = input('Input the index number of the quadrant: ')

# if validate_input(quadrant):
#     print(values[int(quadrant) - 1])
# else:
#     print('Input a number from 1 to 4.')


#-----------------------------------обновлённый код------------------------------------------

# метод для проверки результата ввода числа с консоли
# используем lambda
def validate_input(string):
    bool_check = lambda string: True if string in '1234' else False
    return bool_check

values = ['x > 0, y > 0', 'x < 0, y > 0', 'x < 0, y < 0', 'x > 0, y < 0']
quadrant = input('Input the index number of the quadrant: ')

if validate_input(quadrant):
    print(values[int(quadrant) - 1])
else:
    print('Input a number from 1 to 4.')