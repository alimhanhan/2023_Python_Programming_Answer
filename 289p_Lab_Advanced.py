import random

Computer_Board = []
User_Board = []

for computer in range(10):
    Computer_Board.append(['.'] * 10)

for user in range(11):
    User_Board.append(['.'] * 10)

def main():
    global User_Board
    global Computer_Board

    print_Board(User_Board)

    user_input = input('행과 열을 입력하시오: ')
    x, y = user_input.split(",")
    x, y = int(x), int(y)

    generate_Board(x, y)
    open_tile(x, y)

    while True:
        print_Board(User_Board)
        user_input = input('행과 열을 입력하시오: ')

        x, y = user_input.split(",")
        x, y = int(x), int(y)
        open_tile(x, y)

        if check_victory() == 1:
            exit()


def generate_Board(x, y):
    global Computer_Board
    global User_Board

    for row in range(10):
        for col in range(10):
            if random.random() < 0.3:
                Computer_Board[row][col] = '#'

    for row in range(y - 2, y + 1):
        for col in range(x - 2, x + 1):
            Computer_Board[row][col] = '.'

    for row in range(10):
        for col in range(10):

            Mine_Num = 0
            if Computer_Board[row][col] == '.':
                if 0 <= (row - 1) and (row - 1) <= 9 and 0 <= (col - 1) and (col - 1) <= 9:
                    if Computer_Board[row - 1][col - 1] == '#':
                        Mine_Num += 1
                if 0 <= (row - 1) and (row - 1) <= 9 and 0 <= (col) and (col) <= 9:
                    if Computer_Board[row - 1][col] == '#':
                        Mine_Num += 1
                if 0 <= (row - 1) and (row - 1) <= 9 and 0 <= (col + 1) and (col + 1) <= 9:
                    if Computer_Board[row - 1][col + 1] == '#':
                        Mine_Num += 1
                if 0 <= (row) and (row) <= 9 and 0 <= (col - 1) and (col - 1) <= 9:
                    if Computer_Board[row][col - 1] == '#':
                        Mine_Num += 1
                if 0 <= (row) and (row) <= 9 and 0 <= (col + 1) and (col + 1) <= 9:
                    if Computer_Board[row][col + 1] == '#':
                        Mine_Num += 1
                if 0 <= (row + 1) and (row + 1) <= 9 and 0 <= (col - 1) and (col - 1) <= 9:
                    if Computer_Board[row + 1][col - 1] == '#':
                        Mine_Num += 1
                if 0 <= (row + 1) and (row + 1) <= 9 and 0 <= (col) and (col) <= 9:
                    if Computer_Board[row + 1][col] == '#':
                        Mine_Num += 1
                if 0 <= (row + 1) and (row + 1) <= 9 and 0 <= (col + 1) and (col + 1) <= 9:
                    if Computer_Board[row + 1][col + 1] == '#':
                        Mine_Num += 1

                Computer_Board[row][col] = str(Mine_Num)


def print_Board(board):
    for row in range(10):
        for col in range(10):
            print(board[row][col], end=' ')
        print('')


def open_tile(x, y):
    global User_Board
    global Computer_Board

    if Computer_Board[y - 1][x - 1] == '#':
        User_Board[y - 1][x - 1] = Computer_Board[y - 1][x - 1]
        print_Board(User_Board)
        print('Game over!')
        exit()
    else:
        Continue_Open(x, y)


def Continue_Open(x, y):
    global User_Board
    global Computer_Board
    User_Board[y - 1][x - 1] = Computer_Board[y - 1][x - 1]
    row = x - 1
    col = y - 1

    if Computer_Board[col][row] == '0':
        if 0 <= (col - 1) and (col - 1) <= 9 and 0 <= (row - 1) and (row - 1) <= 9:
            if Computer_Board[col - 1][row - 1] == '0' and User_Board[col - 1][row - 1] == '.':
                Continue_Open(x - 1, y - 1)

        if 0 <= (col - 1) and (col - 1) <= 9 and 0 <= (row) and (row) <= 9:
            if Computer_Board[col - 1][row] == '0' and User_Board[col - 1][row] == '.':
                Continue_Open(x, y - 1)

        if 0 <= (col - 1) and (col - 1) <= 9 and 0 <= (row + 1) and (row + 1) <= 9:
            if Computer_Board[col - 1][row + 1] == '0' and User_Board[col - 1][row + 1] == '.':
                Continue_Open(x + 1, y - 1)

        if 0 <= (col) and (col) <= 9 and 0 <= (row - 1) and (row - 1) <= 9:
            if Computer_Board[col][row - 1] == '0' and User_Board[col][row - 1] == '.':
                Continue_Open(x - 1, y)

        if 0 <= (col) and (col) <= 9 and 0 <= (row + 1) and (row + 1) <= 9:
            if Computer_Board[col][row + 1] == '0' and User_Board[col][row + 1] == '.':
                Continue_Open(x + 1, y)

        if 0 <= (col + 1) and (col + 1) <= 9 and 0 <= (row - 1) and (row - 1) <= 9:
            if Computer_Board[col + 1][row - 1] == '0' and User_Board[col + 1][row - 1] == '.':
                Continue_Open(x - 1, y + 1)

        if 0 <= (col + 1) and (col + 1) <= 9 and 0 <= (row) and (row) <= 9:
            if Computer_Board[col + 1][row] == '0' and User_Board[col + 1][row] == '.':
                Continue_Open(x, y + 1)

        if 0 <= (col + 1) and (col + 1) <= 9 and 0 <= (row + 1) and (row + 1) <= 9:
            if Computer_Board[col + 1][row + 1] == '0' and User_Board[col + 1][row + 1] == '.':
                Continue_Open(x + 1, y + 1)

    if Computer_Board[col][row] == '0':
        if 0 <= (col - 1) and (col - 1) <= 9 and 0 <= (row - 1) and (row - 1) <= 9:
            User_Board[col - 1][row - 1] = Computer_Board[col - 1][row - 1]

        if 0 <= (col - 1) and (col - 1) <= 9 and 0 <= (row) and (row) <= 9:
            User_Board[col - 1][row] = Computer_Board[col - 1][row]

        if 0 <= (col - 1) and (col - 1) <= 9 and 0 <= (row + 1) and (row + 1) <= 9:
            User_Board[col - 1][row + 1] = Computer_Board[col - 1][row + 1]

        if 0 <= (col) and (col) <= 9 and 0 <= (row - 1) and (row - 1) <= 9:
            User_Board[col][row - 1] = Computer_Board[col][row - 1]

        if 0 <= (col) and (col) <= 9 and 0 <= (row + 1) and (row + 1) <= 9:
            User_Board[col][row + 1] = Computer_Board[col][row + 1]

        if 0 <= (col + 1) and (col + 1) <= 9 and 0 <= (row - 1) and (row - 1) <= 9:
            User_Board[col + 1][row - 1] = Computer_Board[col + 1][row - 1]

        if 0 <= (col + 1) and (col + 1) <= 9 and 0 <= (row) and (row) <= 9:
            User_Board[col + 1][row] = Computer_Board[col + 1][row]

        if 0 <= (col + 1) and (col + 1) <= 9 and 0 <= (row + 1) and (row + 1) <= 9:
            User_Board[col + 1][row + 1] = Computer_Board[col + 1][row + 1]


def check_victory():
    global User_Board

    exit_game = 0

    for row in range(10):
        for col in range(10):
            if Computer_Board[row][col] != '#':
                if User_Board[row][col] == Computer_Board[row][col]:
                    exit_game = 1
                else:
                    exit_game = 0
                    return 0

    if exit_game == 1:
        print('Victory!')
        return 1

main()