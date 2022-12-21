# Реализуйте алгоритм перемешивания списка.

from random import randint

while True:
    user_input = input('Input the number of initial list elements, an integer from 10 to 20: ')
    if user_input.isdigit():
        n = int(user_input)
        if n >= 10 and n <= 20:
            break
        else:
            print('Input Error! Try again!')
    else:
            print('Input Error! Try again!')

initial_list = []

for i in range(n):
    initial_list.append(randint(-100, 100))
print(f'The initial list is here: {initial_list}.')

for i in range(n*100):
    index1 = randint(0, n - 1)
    index2 = randint(0, n - 1)
    if index1 == index2 and index1 != n - 1:
        index2 = index1 + 1
    elif index1 == index2 and index1 == n - 1:
        index2 = 0
    temp = initial_list[index1]
    initial_list[index1] = initial_list[index2]
    initial_list[index2] = temp

print(f'The mixed list is here: {initial_list}.')