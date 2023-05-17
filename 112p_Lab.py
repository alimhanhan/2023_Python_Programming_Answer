time = int(input('주당 근무 시간을 입력하시오: '))
wage = float(input('시급을 입력하시오: '))

if time > 40:
    over = time - 40
    total = wage*40 + (wage*1.5)*over
else:
    total = wage * time

print('총 임급은', total, '입니다.')