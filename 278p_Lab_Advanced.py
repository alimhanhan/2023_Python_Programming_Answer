def menu_choice(i):
    if i == 1:
        print(friends)
    elif i == 2:
        name = input('이름을 입력하시오: ')
        friends.append(name)
    elif i == 3:
        del_name = input('삭제할 이름을 입력하시오: ')
        if del_name in friends:
            friends.remove(del_name)
        else:
            print('이름이 친구 목록에 존재하지 않습니다.')
    elif i == 4:
        old_name = input('변경할 이름을 입력하시오: ')
        if old_name in friends:
            index = friends.index(old_name)
            new_name = input('새 이름을 입력하시오: ')
            friends[index] = new_name
        else:
            print('이름이 친구 목록에 존재하지 않습니다.')


menu = 0
friends = []

while menu != 5:
    print('-------------------')
    print('1. 친구 리스트 출력')
    print('2. 친구 추가')
    print('3. 친구 삭제')
    print('4. 이름 변경')
    print('5. 종료')

    menu = int(input('메뉴를 선택하시오: '))
    menu_choice(menu)
