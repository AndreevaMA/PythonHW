# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

#------------------------------------исходный код------------------------------------------
# my_list = []
# for i in range(randint(8, 9)):
#     my_list.append(randint(-10, 10))
# print(my_list)

# oddsum_list = []

# if len(my_list) % 2 == 0:
#     el_num = int(len(my_list) / 2)
# else:
#     el_num = int(len(my_list) / 2 + 0.5)

# for i in range(el_num):
#     oddsum_list.append(my_list[i] * my_list[len(my_list) - 1 - i])
# print(oddsum_list)

#-----------------------------------обновлённый код------------------------------------------

# используем list comprehension
my_list = [randint(-10, 10) for i in range(randint(8, 9))]
print(my_list)

if len(my_list) % 2 == 0:
    el_num = int(len(my_list) / 2)
else:
    el_num = int(len(my_list) / 2 + 0.5)

# используем list comprehension
oddsum_list = [my_list[i] * my_list[len(my_list) - 1 - i] for i in range(el_num)]
print(oddsum_list)
