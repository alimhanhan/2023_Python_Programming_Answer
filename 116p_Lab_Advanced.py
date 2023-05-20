ach = int(input('실적을 입력하시오: '))
goal = int(input('실적 목표를 입력하시오: '))

if ach <= goal:
    print('실적 달성 보너스는 0원입니다.')
else:
    bonus = ach - goal
    final_bonus = bonus * 0.1
    print('실적 달성 보너스: ', final_bonus)