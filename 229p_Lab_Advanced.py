def bigger(a, b):
    if a >= b:
        return a, b
    else:
        return b, a

num1 = int(input('첫 번째 수를 입력하시오: '))
num2 = int(input('두 번째 수를 입력하시오: '))

print(bigger(num1, num2))