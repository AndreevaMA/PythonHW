# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# -----------------------------РЕШЕНИЕ-----------------------------

# ------------------------------МЕТОДЫ-----------------------------

# метод для считывания содержимого исходных файлов
def file_read(file_name):
    path = file_name
    data = open(path, 'r')
    for line in data:
        poly = line
    data.close()
    return poly

# метод превращения многочлена в список, разбивка на элементы по знаку " + "
def str_to_list(poly):
    poly_list = poly.split(' + ')
    for i in range(len(poly_list)):
        if poly_list[i].startswith('x'):
            poly_list[i] = '1 * ' + poly_list[i]
    return poly_list

# выделение отдельного списка с ключами будущего словаря
def list_to_keys(a_list):
    poly_keys = []
    for i in range(len(a_list) - 1):
        temp_list = a_list[i].split(' * ')
        poly_keys.append(temp_list[1])
    poly_keys.append('zero')
    return poly_keys

# выделение отдельного списка со значениями будущего словаря
def list_to_nums(a_list):
    poly_nums = []
    for i in range(len(a_list) - 1):
        temp_list = a_list[i].split(' * ')
        poly_nums.append(temp_list[0])
    poly_nums.append(a_list[len(a_list) - 1])
    return poly_nums

# создание словаря на основе списка ключей и списка значений
def create_dict(keys_list, nums_list):
    my_dict = {}
    for i in range(len(keys_list)):
        my_dict[keys_list[i]] = nums_list[i]
    return my_dict

# метод выделения максимальной степени x в списке ключей
def poly_power(keys_list):
    if keys_list[0].startswith('x^'):
        a_pow = int(keys_list[0].replace('x^', ''))
    else:
        a_pow = int(keys_list[0].replace('x', ''))
    return a_pow


# ---------------------------ОСНОВНОЕ РЕШЕНИЕ--------------------------

# считываем данные из файлов
poly1 = file_read('Poly1.txt')
poly2 = file_read('Poly2.txt')
print(f'poly1: {poly1}.')
print(f'poly2: {poly2}.')

# превращаем многочлены в списки
poly1_list = str_to_list(poly1)
poly2_list = str_to_list(poly2)

# выделяем ключи и значения для словарей
poly1_nums = list_to_nums(poly1_list)
poly2_nums = list_to_nums(poly2_list)
poly1_keys = list_to_keys(poly1_list)
poly2_keys = list_to_keys(poly2_list)

# создаём словари
poly1_dict = create_dict(poly1_keys, poly1_nums)
poly2_dict = create_dict(poly2_keys, poly2_nums)
print(poly1_dict)
print(poly2_dict)

# определяем основной и дополняющий словарь
# создаём временный словарь для определения результирующих "ключей" финального списка
pow1 = poly_power(poly1_keys)
pow2 = poly_power(poly2_keys)
temp_dict = {}
if pow1 >= pow2:
    temp_dict = poly1_dict.copy()
    temp_dict.update(poly2_dict)
else:
    temp_dict = poly2_dict.copy()
    temp_dict.update(poly1_dict)
sum_dict_keys = list(temp_dict.keys())
print(f'The x-elements of the resulting polynomial are: {sum_dict_keys}.')

# высчитываем результирующие "значения" для финального списка
sum_dict_nums = []
for i in range(len(sum_dict_keys)):
    sum_dict_nums.append(int(poly1_dict.get(sum_dict_keys[i], 0)) + int(poly2_dict.get(sum_dict_keys[i], 0)))
print(f'The coefficients of the resulting polynomial are: {sum_dict_nums}.')

# создание финального списка из результирующих списков "ключей" и "значений"
sum_poly = []
for i in range(0, len(sum_dict_keys) - 1):
    if sum_dict_nums[i] == 1:
        sum_poly.append(f'{sum_dict_keys[i]}')
    else:
        sum_poly.append(f'{str(sum_dict_nums[i])} * {sum_dict_keys[i]}')
sum_poly.append(f'{sum_dict_nums[len(sum_dict_keys) - 1]}')

# создание результирующего многочлена из финального списка
final_poly = sum_poly[0]
for i in range(1, len(sum_poly)):
    final_poly = final_poly + ' + ' + sum_poly[i]
print(final_poly)

# запись в файл
data = open('poly_task5.txt', 'a')
data.writelines(final_poly)
data.close()









