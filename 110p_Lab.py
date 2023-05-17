money = float(input("구입 금액: "))
total = money

if money > 100000:
    total = money - (money * 0.05)
    print('지불하실 금액:', total)
else:
    print('지불하실 금액:', total)