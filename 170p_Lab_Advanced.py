sum = 0

for i in range(1, 101, 1):
    if ( i % 3 == 0 ):
        sum = sum + i
    else:
        continue

print('1부터 100 사이의 모든 3의 배수의 합은 ', sum, '입니다.', sep='')