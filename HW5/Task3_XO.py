# Cоздайте программу для игры в "Крестики-нолики".


# хранилище статусов каждой ячейки игрового поля
values = list(range(1, 10))


# метод, выводящий на консоль текущие значения каждой ячейки игрового поля
def playing_field(values):
    print()
    print('-' * 19)
    print(f'|  {values[0]}  |  {values[1]}  |  {values[2]}  |') 
    print('-' * 19)
    print(f'|  {values[3]}  |  {values[4]}  |  {values[5]}  |') 
    print('-' * 19)
    print(f'|  {values[6]}  |  {values[7]}  |  {values[8]}  |')
    print('-' * 19)
    print()


# метод ввода хода текущим игроком и его валидация
def the_move(current_player, tic_tac):
    while True:
        print(f'{current_player}, ваш ход. Выберите клетку, чтобы поставить {tic_tac}: ', end = '')

        # обработка непредусмотренного ввода
        try:
            player_input = int(input())
        except ValueError:
            print('Выберите номер незанятой клетки игрового поля: ')
            print()
            continue
        
        # валидация на корректность номера ячейки и на вакантность ячейки
        if player_input >= 1 and player_input <= 9:
            if(str(values[player_input - 1]) not in 'XO'):
                values[player_input - 1] = tic_tac
                break
            else:
                print('Эта клетка игрового поля уже занята.')
                print()
        else:
            print('Попробуйте ещё раз.')
            print()


# метод, проверяющий общий статус игрового поля на победу или поражение одного из игроков
def victory_check(values):

    # все возможные победные комбинации
    victory = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    
    for combo in victory:
        if values[combo[0]] == values[combo[1]] == values[combo[2]]:
            return True
    return False


# игра
def main(values):
    print('Сыграем в крестики-нолики!')
    print()

    player1 = input('Игрок 1, введите ваше имя: ')
    while True:
        player2 = input('Игрок 2, введите ваше имя: ')
        if player1 == player2:
            print(f'Ошибка! Игрок {player1} уже в игре! Введите другое имя!')
        else:
            break

    print()

    move_counter = 0

    while True:
        playing_field(values)

        if move_counter % 2 == 0:
            current_player = player1
            the_move(current_player, 'X')
        else:
            current_player = player2
            the_move(current_player, 'O')

        if move_counter > 3:
            game_end = victory_check(values)
            if game_end:
                print(f'{current_player}, вы победили!')
                playing_field(values)
                break
            if move_counter == 8:
                print('Ничья!')
                playing_field(values)
                break

        move_counter += 1


main(values)
    
