print("숫자 게임을 시작합니다.")

num = 52
s = input("1~100 사이의 수를 입력하시오: ")

answer  =int(s)
if answer == num:
    print("정답입니다!")
else:
    print("오답입니다.")

print("게임을 종료합니다.")