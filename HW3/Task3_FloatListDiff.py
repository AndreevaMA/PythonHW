# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []
for i in range(random.randint(5, 10)):
    my_list.append(round(random.random() * 100, 2))
print(my_list)

list_no_int = [] # в указанном примере число 5 считается числом без дробной части
for i in my_list:
    if i % 1 != 0:
        list_no_int.append(i)
print(list_no_int)

min_fractional = round(list_no_int[0] % 1, 2)
max_fractional = round(list_no_int[0] % 1, 2)
for i in list_no_int:
    if i % 1 < min_fractional:
        min_fractional = round(i % 1, 2)
    elif i % 1 > max_fractional:
        max_fractional = round(i % 1, 2)

delta = round(max_fractional - min_fractional, 2)
print(f'The difference between the biggest fractional part {max_fractional}\
    and the smallest fractional part {min_fractional} is equal to {delta}.')