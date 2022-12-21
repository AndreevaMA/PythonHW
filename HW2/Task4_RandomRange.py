# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем позициях.

#----------------------------------------METHODS----------------------------------------

#------------------------------------Input integer--------------------------------------
def InputInteger(invitation_text, condition_text):
    print(invitation_text)
    while True:
        user_input = input(condition_text)
        if user_input.isdigit():
            x = int(user_input)
            return x
        else:
            print('Input Error! Try again!')


#-------------------------------------Program start-------------------------------------

n = InputInteger('Input the number of elements of the new list.', 'Input an integer > 0: ')
n_list = []

from random import random

for i in range(n):
    n_list.append(round(random() * (n - (-n)) + (-n),1))
print(n_list)

while True:
    pos1 = InputInteger('Input the position of the 1st factor.', f'Input an integer from 0 to {n - 1}: ')
    if pos1 >= 0 and pos1 <= n - 1:
        break
    else:
        print('Input Error! Try again!')

while True:
    pos2 = InputInteger('Input the position of the 2nd factor.', f'Input an integer from 0 to {n - 1}: ')
    if pos2 >= 0 and pos2 <= n - 1:
        break
    else:
        print('Input Error! Try again!')

num_product = n_list[pos1] * n_list[pos2]
print(f'The product of 1st factor (#{pos1}: {n_list[pos1]}) and the 2nd factor (#{pos2}: {n_list[pos2]}) is equal to {num_product}.')


#--------------------------------------Program end--------------------------------------