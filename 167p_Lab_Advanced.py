number = int(input('숫자를 입력하세요: '))
fac = 1

for i in range(1, number+1, 1):
    fac = fac * i

print(number, '!의 결과는 ', fac, '입니다.', sep='')