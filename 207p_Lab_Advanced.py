import math

def sphere(radius):
    vol = (4.0 / 3.0) * math.pi * radius * radius *radius
    return vol

ten = sphere(10.0)
twenty = sphere(20.0)

print('반지름이 10.0인 구의 부피:', ten)
print('반지름이 20.0인 구의 부피:', twenty)