def get_fac(n):
    sum = 1
    for i in range(n, 1, -1):
        sum = sum * i
    return sum

number = int(input('숫자를 입력하시오: '))
final = get_fac(number)

print(number, '! = ', final, sep='')