credit = int(input('이수한 학점 수: '))

if credit >= 140:
    gpa = float(input('평점: '))
    if gpa >= 2.0:
        print('졸업 가능')
    else:
        print('졸업 불가')
else:
    print('졸업 불가')