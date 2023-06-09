board = [[' ' for x in range (3)] for y in range(3)]

def print_board():
    for r in range(3):
        print("  " + board[r][0] + "|  " + board[r][1] + "|  " + board[r][2])
        if (r != 2):
            print("---|---|---")

def victory_check():
    if board[0][0] != ' ' and board[1][1] == board[0][0] == board[2][2]:
        return 10
    elif board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return 10
    elif board[0][0] != ' ' and board[0][0] == board[1][0] == board[2][0]:
        return 10
    elif board[0][1] != ' ' and board[0][1] == board[1][1] == board[2][1]:
        return 10
    elif board[0][2] != ' ' and board[0][2] == board[1][2] == board[2][2]:
        return 10
    elif board[0][0] != ' ' and board[0][0] == board[0][1] == board[0][2]:
        return 10
    elif board[1][0] != ' ' and board[1][0] == board[1][1] == board[1][2]:
        return 10
    elif board[2][0] != ' ' and board[2][0] == board[2][1] == board[2][2]:
        return 10
    else:
        return 20

while True:
    print_board()

    # 사용자로부터 좌표 입력받기
    x = int(input("다음 수의 x좌표를 입력하시오: "))
    y = int(input("다음 수의 y좌표를 입력하시오: "))

    if board[x][y] != ' ':
        print('잘못된 위치입니다. ')
        continue
    else:
        board[x][y] = 'X'

    if victory_check() != 20:
        print_board()
        print('사용지 승리')
        break

    # 컴퓨터가 대각선 방향을 먼저 선점하도록 코드 추가
    done = False
    for a in range(3):
        if board[a][a] == ' ' and not done:
            board[a][a] = 'O'
            done = True
            break

    # 만약 대각선 공간이 다 차고 없으면 첫 번째로 발견하는 공란 선택
    if done == False:
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ' and not done:
                    board[i][j] = 'O'
                    done = True
                    break

    if victory_check() != 20:
        print_board()
        print('컴퓨터 승리')
        break