class Car:
    def __init__(self, speed=0, gear=1, fuel=0, distance=0, color="white"):
        self.__speed = speed
        self.__gear = gear
        self.__color = color
        self.__fuel = fuel
        self.__distance = distance

    def setSpeed(self, speed):
        self.__speed = speed

    def setGear(self, gear):
        self.__gear = gear

    def setColor(self, color):
        self.__color = color

    def Fuel_efficiency(self, fuel):
        self.__fuel = fuel

    def set_distance(self, distance):
        self.__distance = distance

    def __str__(self):
        return '(속도: %d, 기어: %d, 연비: %d, 색상: %s)\n%dkm 주행 시 필요 연료: %dL' \
            % (self.__speed, self.__gear, self.__fuel, self.__color, self.__distance, (self.__distance / self.__fuel))

myCar = Car()
myCar.setGear(3)
myCar.setSpeed(100)
myCar.Fuel_efficiency(100)
myCar.set_distance(int(input('주행 거리: ')))

print('자동차 정보:', myCar)