# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Примеры: 45 -> 101101, 3 -> 11, 2 -> 10

from random import randint

n = randint(-10000, 10000)
abs_n = abs(n)
print(f'The number is {n}, its abs is {abs_n}.')

result = 0
number = 0
multiplier = 1

while(abs_n > 0):
    number = int(abs_n % 2)
    abs_n = int(abs_n / 2)
    result = result + number * multiplier
    multiplier *= 10

if (n >= 0):
    print(f'The number transformed is {result}.')
else:
    print(f'The number transformed is 1{result}.')
