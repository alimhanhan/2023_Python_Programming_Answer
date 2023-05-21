age = int(input('나이를 입력하시오: '))

if age >= 51:
    print('노년기입니다.')
elif age >= 31:
    print('장년기입니다.')
elif age >= 19:
    print('청년기입니다.')
elif age >= 13:
    print('청소년기입니다.')
else:
    print('어린이입니다.')