# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = randint(1, 10)
print(k)

poly_list_1 = [str(randint(0, 100)), ] # элемент без х

# так как минимальное k = 1, добавляем элемент формата b * x
# при этом если k = 1, то это будет самый первый элемент и его коэффициент не может быть равен нулю
if k == 1:
    new_index = str(randint(1, 100))
    new_monomial = str(f' * x')
    new_element = new_index + new_monomial
    poly_list_1.append(new_element)
else:
    new_index = str(randint(0, 100))
    new_monomial = str(f' * x')
    new_element = new_index + new_monomial
    poly_list_1.append(new_element)

# далее если k > 1, добавляем оставшиеся элементы многочлена
# сразу предусмотрим, что самый первый элемент и его коэффициент не может быть равен нулю
if k == 2:
    new_index = str(randint(1, 100))
    new_monomial = str(f' * x^2')
    new_element = new_index + new_monomial
    poly_list_1.append(new_element)
elif k != 2 and k != 1:
    for i in range(2, k):
        new_index = str(randint(0, 100))
        new_monomial = str(f' * x^{i}')
        new_element = new_index + new_monomial
        poly_list_1.append(new_element)
    new_index = str(randint(1, 100)) # коэффициент самого первого элемента не может быть равен нулю
    new_monomial = str(f' * x^{k}')
    new_element = new_index + new_monomial
    poly_list_1.append(new_element)

print(poly_list_1)

# разворачиваем список, удаляя при этом элементы, коэффициенты при которых равны нулю
# а также форматируем элементы, индекс которых равен 1
poly_list_2 = []
for i in range(len(poly_list_1) - 1, -1, -1):
    if not poly_list_1[i].startswith('0'):
        if not poly_list_1[i].startswith('1 * '):
            poly_list_2.append(poly_list_1[i])
        else:
            poly_list_2.append(poly_list_1[i].replace('1 * ',''))
print(poly_list_2)

# создание непосредственно многочлена
my_poly = str(poly_list_2[0])
for i in range(1, len(poly_list_2)):
    my_poly = my_poly + ' + ' + poly_list_2[i]
my_poly = my_poly + ' = 0'
print(my_poly)

# запись в файл
data = open('poly.txt', 'a')
data.writelines(my_poly)
data.close()


