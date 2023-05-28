year = int(input('년도를 입력하시오: '))

if year % 400 == 0:
    print(year, '년은 윤년입니다.', sep='')
elif year % 100 == 0:
    print(year, '년은 윤년이 아닙니다.', sep='')
elif year % 4 == 0:
    print(year, '년은 윤년입니다.', sep='')
else:
    print(year, '년은 윤년이 아닙니다.', sep='')