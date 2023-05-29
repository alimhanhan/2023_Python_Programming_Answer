a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

for i in range(-10000, +10000):
    if ((a*i*i) + (b*i) + c) == 0:
        answer = i
        break

print(a, 'x*x + ', b, 'x + ', c, ' = 0 의 근은 ', answer, '이다.',sep='')

