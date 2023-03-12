print("숫자 게임을 시작합니다.")

num = 52

while True:
    s = input("1~100 사이의 수를 입력하시오: ")
    answer = int(s)

    if answer == num:
        print("정답입니다! 게임을 종료합니다.")
        break
    else:
        if answer > num:
            print("오답입니다. 조금 더 작은 수를 선택하세요.")
        else:
            print("오답입니다. 조금 더 큰 수를 선택하세요.")