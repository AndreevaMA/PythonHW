# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

while True:
    try:
     user_input = float(input('Input a real number: '))
     break
    except ValueError:
      print('Input Error! Try again!', end = ' ')
    
print(f'Initial user input: {user_input}.')
num = abs(user_input)
str_num = str(num)
str_num = str_num.replace('.', '')

num_len = len(str_num)
sum_digits = 0
for i in range(num_len):
    sum_digits = sum_digits + int(str_num[i])
print(f'Sum of digits: {sum_digits}.')