number = int(input('숫자를 입력하시오: '))

for i in range(1, 10, 1):
    result = number * i
    print(number, 'x', i, '=', result)