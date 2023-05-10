number = int(input("짐 개수: "))
total = 0
cnt = 1

for i in range (0, number):
    weight = int(input("짐 무게: "))

    if (weight > 20) and (cnt == 1):
        total = total + 20000
        cnt = 0
    else:
        continue

if number >= 2:
    total = total + 30000
else:
    total = total

print("납부하실 총 금액은", total, "원입니다.\n")