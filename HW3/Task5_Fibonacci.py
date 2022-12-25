# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 7 список будет выглядеть так: [13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13]

from random import randint

n = randint(5, 10)
print(n)

fibo_list = []
for i in range(n * 2 + 1):
    fibo_list.append(0)
print(fibo_list)

fibo_list[n] = 0
fibo_list[n + 1] = 1
fibo_list[n - 1] = -1

for i in range(n - 1):
    fibo_list[n + 2 + i] = fibo_list[n + 2 + i - 1] + fibo_list[n + 2 + i - 2]
    fibo_list[n - 2 - i] = fibo_list[n + 2 + i] * ((-1)**(n + 2 + i + 1))

print(fibo_list)
