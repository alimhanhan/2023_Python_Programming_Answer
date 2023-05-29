h = float(input('원기둥의 높이를 입력하시오: '))
pi = 3.14
r = float(input('원기둥의 밑면의 원의 반지름을 입력하시오: '))

surface_area = (2.0 * pi * r * r) + (2.0 * pi * r * h)
volume = 2.0 * pi * r * r

print('원기둥의 표면적: ', surface_area)
print('원기둥의 부피: ', volume)