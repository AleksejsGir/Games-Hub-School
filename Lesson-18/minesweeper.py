# Игра: Сапёр
import random


def game_board(size, mines):
    board = [['-' for _ in range(size)] for _ in range(size)]
    mine_positions = set()
    while len(mine_positions) < mines:
        mine_positions.add((random.randint(0, size - 1), random.randint(0, size - 1)))
    for (x, y) in mine_positions:
        board[x][y] = '*'
    return board, mine_positions


def print_board(board):
    for row in board:
        print(' '.join(row))
    print()


def count_mines(board, x, y):
    size = len(board)
    count = 0
    for i in range(max(0, x - 1), min(size, x + 2)):
        for j in range(max(0, y - 1), min(size, y + 2)):
            if board[i][j] == '*':
                count += 1
    return count


def minesweeper(size=5, mines=5):
    board, mine_positions = game_board(size, mines)
    opened_board = [['-' for _ in range(size)] for _ in range(size)]
    safe_cells = size * size - mines
    opened_cells = 0

    while opened_cells < safe_cells:
        print_board(opened_board)
        x, y = map(int, input("Введите координаты клетки (строка столбец): ").split())
        if (x, y) in mine_positions:
            print("Вы проиграли! Вы попали на мину.")
            print_board(board)
            return
        if opened_board[x][y] == '-':
            mines_count = count_mines(board, x, y)
            opened_board[x][y] = str(mines_count)
            opened_cells += 1


    print("Поздравляем! Вы открыли все безопасные клетки.")
    print_board(opened_board)

if __name__ == "__main__":
    minesweeper()
    print("Модуль запущен на прямую.")

# Цель игры: открыть все клетки, не содержащие мин.
#
# Правила игры:
#
# 1. Игровое поле состоит из клеток размером 5x5.
# 2. На поле случайным образом размещены 5 мин.
# 3. Игрок вводит координаты клетки (например, "2 3" для второй строки и третьего столбца), чтобы проверить ее.
# 4. Если игрок открывает клетку с миной, он проигрывает.
# 5. Если игрок открывает клетку без мины, на этой клетке отображается число, указывающее, сколько мин находится в соседних клетках (по горизонтали, вертикали и диагоналям).
# 6. Игрок побеждает, если открывает все клетки, не содержащие мин.
#
# Пример игрового процесса:
#
# 1. Игроку показывается пустое поле:
# - - - - -
# - - - - -
# - - - - -
# - - - - -
# - - - - -
#
# 2. Игрок вводит координаты клетки:
# Введите координаты клетки (строка столбец): 2 3
#
# 3. Если в этой клетке нет мины, открывается число:
# - - - - -
# - - 1 - -
# - - - - -
# - - - - -
# - - - - -
#
# 4. Игрок продолжает вводить координаты, пока не откроет все безопасные клетки или не попадет на мину.
# 5. Если игрок открывает клетку с миной, игра заканчивается:
# - - - - -
# - - * - -
# - - - - -
# - - - - -
# - - - - -
# Вы проиграли! Вы попали на мину.
#
# 6. Если игрок открывает все клетки без мин, игра заканчивается победой:
# - 1 1 1 -
# - 1 * 1 -
# - 2 2 2 -
# - 1 * 1 -
# - 1 1 1 -
# Поздравляем! Вы открыли все безопасные клетки.