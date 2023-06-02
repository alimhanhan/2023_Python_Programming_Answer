print('주사위 2개를 던졌을 때 합이 6이 되는 경우: ')

for i in range(1,7,1):
    for a in range(1,7,1):
        if (i + a == 6):
            if a == 1:
                print('(', i, ', ', a, ')', sep='', end=" ")
            else:
                print('(', i, ', ', a, '),', sep='', end=" ")
        else:
            continue