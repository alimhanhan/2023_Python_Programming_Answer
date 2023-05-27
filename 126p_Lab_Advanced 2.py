year = int(input('년을 입력하시오: '))
month = input('월을 입력하시오: ')

if month == '2월':
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print('2월의 날수는 29일', sep='')
    else:
        print('2월의 날수는 28일', sep='')
elif month == '4월' or month == '6월' or month == '9월' or month == '11월':
    print(month, '의 날수는 30일', sep='')
else:
    print(month, '의 날수는 31일', sep='')