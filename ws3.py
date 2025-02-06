# ws 3

class Car():
    def __init__(self, year, make):
        self.__ModelYear = year
        self.__Make = make
        self.speed = 0

    def accelerate(self):
        self.speed +=5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

    def __repr__(self):
        return "Speed: {}".format(self.speed)

car1 = Car(10, "kia")

for x in range(5):
    car1.accelerate()
    print(car1)

for x in range(5):
    car1.brake()
    print(car1)





