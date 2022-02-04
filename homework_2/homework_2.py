"""
Игра "Обратные Крестики-Нолики"
Поле со значениями имеет размер 10x10
Условия поражения: игрок не создал ряд из 5 своих фигур (горизонтально, вертикально, диагонально)
В игре участвует двое - один игрок(человек), другой компьютер
"""


def get_board(board, next_player):
    """Получение текущего игрового поля с его внутренними значениями"""

    for i in range(len(board)):
        for j in range(len(board[i])):
            # Условия для проверки значения строки, для форматирования вывода
            if i == 0:
                print(str(board[i][j]) + "  | ", end='')
            else:
                print(str(board[i][j]) + " | ", end='')
        if i != 9:
            print()
            print("---|", end='')
            print("----|" * 9)

    print("\nСейчас ход - ", next_player)


def replace_position(board, marker):
    """Функция замены числового значения на маркер"""
    position = int(input("Введите номер клетки для заполнения: "))

    flag = False  # Флаг для проверки выполнения условия
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == position:
                board[i][j] = marker
                flag = True
                break
        if flag:
            break


def player_input(marks):
    """Функция для выбора символа игроком"""
    print('---Добро пожаловать в игру "Обратные Крестики-Нолики---\n\n')

    computer_mark = ''
    while True:
        player_mark = input("Введите Ваш символ для игры (X / O): ").upper()

        if player_mark not in marks:
            print("Вы ввели некорректное значение")
            continue

        computer_mark = marks[1] if player_mark == marks[0] else marks[0]

        return player_mark, computer_mark


def main_game(board, marks):
    """Главная функция игры"""
    player, computer = player_input(marks)
    next_player = player
    while True:
        get_board(board, next_player)
        replace_position(board, next_player)

        next_player = computer if next_player == player else player


GAME_BOARD = [[(j * 10) + i for i in range(1, 11)] for j in range(10)]  # Генерация матрицы игрового поля
MARKS = ('X', 'O')

main_game(GAME_BOARD, MARKS)

"""
1 - Функция проверки занятости ячейки - 
2 - Функция рандомного выбора символа - 
3 - Функция / Функции проверки на поражение - 
4 - Функция проверку на ничью - 
5 - Фунция проверки на правильность ввода числа (от 1 до 100 включительно) - 
6 - Функция очистки экрана - 
7 - Функция переключения игроков -
8 - Функция выбора компьютера - 

"""
