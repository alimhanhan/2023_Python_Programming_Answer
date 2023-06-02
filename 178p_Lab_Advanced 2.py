print('주사위 3개를 던졌을 때 합이 10이 되는 경우: ')
cnt = 0

for i in range(1,7,1):
    for a in range(1,7,1):
        for b in range(1,7,1):
            if (i + a + b == 10):
                if cnt != 0 and cnt % 4 == 0:
                    print('\n')
                if b == 1 and a == 3:
                    print('(', i, ', ', a, ', ', b, ')', sep='', end=" ")
                else:
                    print('(', i, ', ', a, ', ', b, '),', sep='', end=" ")
                cnt = cnt +1
            else:
                continue