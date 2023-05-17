money = float(input("구입 금액: "))
total = money

if money > 100000:
    total = money - (money * 0.05)
    print('지불하실 금액:', total)
else:
    more = 100000 - money
    print('지불하실 금액:', total)
    print(more, '원을 더 소비하시면 5% 할인가가 적용됩니다.')