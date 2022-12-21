# Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
# Пример: Для n = 4: {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}. Сумма 9.06.

while True:
    user_input = input('Input an integer > 0: ')
    if user_input.isdigit():
        n = int(user_input)
        break
    else:
        print('Input Error! Try again!')

subseq = {}
sum_numbers = 0
for i in range(1, n + 1):
    subseq[i] = round((1 + 1 / i) ** i,2)
    sum_numbers = sum_numbers + subseq[i]

print(f'For n = {n}: {subseq}. Sum of elements of the subsequence is equal to {sum_numbers}.')
