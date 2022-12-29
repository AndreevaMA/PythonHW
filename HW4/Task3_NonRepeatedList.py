# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

num_q = randint(10, 20)

initial_list = []
for i in range(num_q):
    initial_list.append(randint(0, 15))
initial_list = list(map(str, initial_list))
print(initial_list)

non_repeated = []
non_repeated.append(initial_list[0])

for i in range(1, num_q):
    if initial_list.count(initial_list[i]) == 1:
        non_repeated.append(initial_list[i])
print(f'The list of unique numbers in the initial list is here: {list(map(int, non_repeated))}.')