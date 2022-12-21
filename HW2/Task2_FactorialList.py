# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

while True:
    user_input = input('Input an integer > 0: ')
    if user_input.isdigit():
        n = int(user_input)
        break
    else:
        print('Input Error! Try again!')
 
factorial = 1
argument_list = ['1']
factorial_list = [1]
for i in range(1, n):
    argument_list.append(f'{argument_list[i - 1]}*{i + 1}')
    factorial = factorial * (i + 1)
    factorial_list.append(factorial)
print(f'If n is equal to {n} then {factorial_list} {tuple(argument_list)}.')