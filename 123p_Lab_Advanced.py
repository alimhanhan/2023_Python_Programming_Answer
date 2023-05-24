user_list = ['가나다', '라마바', '사아자']
pass_list = ['111', '222', '333']

name = input('아이디: ')
if name in user_list:
    password = input('패스워드: ')
    if password in pass_list:
        print('환영합니다.')
    else:
        print('잘못된 패스워드입니다.')
else:
    print('확인되지 않은 사용자입니다.')