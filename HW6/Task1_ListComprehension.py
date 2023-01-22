# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

#------------------------------------исходный код------------------------------------------
# my_list = []
# for i in range(10):
#     my_list.append(randint(-100, 100))
# print(my_list)

# sum = 0
# for i in range(1, len(my_list), 2):
#     sum += my_list[i]
# print(f'Sum of odd-index elemens is equal to {sum}.')

#-----------------------------------обновлённый код------------------------------------------

# используем list comprehension
my_list = [randint(-100, 100) for i in range(10)]
print(my_list)

sum = 0
for i in range(1, len(my_list), 2):
    sum += my_list[i]
print(f'Sum of odd-index elemens is equal to {sum}.')