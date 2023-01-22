# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

#---------------------------------------------------------------------------------------------

from random import randint

# метод осуществления хода игроком (человеком)
def take_sweets(player_name):
    sweets_num = input(f'{player_name}, сколько вы возьмёте конфет? Возьмите не больше 28: ')
    while (not sweets_num.isdigit()) or int(sweets_num) < 1 or int(sweets_num) > 28:
        print('Шутить изволите? :) Давайте-ка ещё разок!')
        sweets_num = input(f'{player_name}, сколько вы возьмёте конфет? Возьмите не больше 28: ')
    return int(sweets_num)

# метод вывода на консоль промежуточного результата
def move_result(player_name, x, y, z):
    print(f'После хода {player_name}, взявшего {x} конфет, у него суммарно {y} конфет. \
        На столе осталось {z} конфет.')

# метод совершения хода умным ботом (с возможностью ошибки бота)
def bot_move(z, numbers):
    mistake_chance = randint(1, 5)
    x = 0
    if str(mistake_chance) in '1234':
        for i in range(1, 29):
            if (z - i) in numbers:
                x = i
    else:
        x = randint(1, 28)
    return x


# игра
print('Сыграем в игру?')

while True:
    mode = input('Выберите игровой режим:\n \
        a - два игрока, b - игра с ботом, c - игра с умным ботом: ')
    print()

    if mode in 'abc':
        break
    else:
        print('Ошибка! Попробуйте ещё раз: ')

if mode == 'a':
    print('Выбран режим "Игра с человеком"')
    player1 = input('Введите имя первого игрока: ')
    while True:
        player2 = input('Введите имя второго игрока: ')
        if player1 == player2:
            print(f'Ошибка! Игрок {player1} уже в игре! Введите другое имя!')
        else:
            break
elif mode == 'b':
    print('Выбран режим "Игра с ботом"')
    player1 = input('Введите имя первого игрока: ')
    player2 = 'Stupid_bot'
else:
    print('Выбран режим "Игра с умным ботом"')
    player1 = input('Введите имя первого игрока: ')
    player2 = 'Clever_bot'
print()

leftover = 2021
print(f'На столе лежит {leftover} конфет.')

col = []
col_add = 29
while col_add <= leftover:
    col.append(col_add)
    col_add += 29

flag = randint(0, 2)  # очередность хода
if flag:
    print(f'В этой игре первый ход делает {player1}.')
else:
    print(f'В этой игре первый ход делает {player2}.')

on_hand1 = 0
on_hand2 = 0

while leftover > 28:
    if flag:
        qty = take_sweets(player1)
        on_hand1 += qty
        leftover -= qty
        flag = False
        move_result(player1, qty, on_hand1, leftover)
    else:
        if mode == 'a':
            qty = take_sweets(player2)
        elif mode == 'b':
            qty = randint(1, 28)
        else:
            qty = bot_move(leftover, col)
        on_hand2 += qty
        leftover -= qty
        flag = True
        move_result(player2, qty, on_hand2, leftover)

if flag:
    print(f'Победитель {player1}.')
else:
    print(f'Победитель {player2}.')