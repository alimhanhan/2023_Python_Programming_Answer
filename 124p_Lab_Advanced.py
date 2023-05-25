number = input('숫자를 입력하시오: ')
han1 = ['일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

if len(number) >= 3:
    for i in range(0, 9):
        if number[0] == num[i]:
            three = han1[i] + '백'

    for i in range(0, 9):
        if number[1] == num[i]:
            two = han1[i] + '십'

    for i in range(0, 9):
        if number[2] == num[i]:
            one = han1[i]

    print(three, two, one)

elif len(number) >= 2:
    for i in range(0, 9):
        if number[0] == num[i]:
            two = han1[i] + '십'
            break

    for i in range(0, 9):
        if number[1] == num[i]:
            one = han1[i]
            break

    print(two, one)
else:
    for i in range(0, 9):
        if number[0] == num[i]:
            one = han1[i]
            break

    print(one)