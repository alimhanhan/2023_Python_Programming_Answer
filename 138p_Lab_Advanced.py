answer = 5
print('숫자 게임에 오신 것을 환영합니다!')

while True:
    g = int(input('숫자를 맞춰보세요!: '))

    if g == answer:
        print('정답입니다!')
        break
    else:
        if g > answer:
            print('조금 더 작은 수를 선택해보세요!')
        else:
            print('조금 더 큰 수를 선택해보세요!')

print('게임을 종료합니다.')