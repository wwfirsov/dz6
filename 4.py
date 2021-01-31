class Car:

    speed = 0
    color = "none"
    name = "none"
    is_police = True

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(direction):
        print('Машина повернулась (куда?!)')
    def show_speed(self):
        print('Текущая скорость автомобиля', speed)

class TownCar(Car):
    def show_info(self, speed, color, name):
        print('Городская машина')
        self.speed = speed
        self.color = color
        self.name = name

    def show_speed(self, speed):
        if speed > 60:
            print('Текущая скорость городской машины', speed)
            print('Превышение скорости')

class SportCar(Car):
        print('Спортивная машина')

class WorkCar(Car):
    def show_speed(self):
        print('Рабочая машина')
        if speed < 40:
            print('Текущая скорость рабочей машины', speed)
            print('Превышение скорости')

class PoliceCar(Car):
    print('Полицейская машина')


tc = TownCar()

print('Городская машина')
speed = int(input('Введите скорость: '))
tc.show_info(speed, "red", "zaz")
tc.show_speed(speed)



# sc = SportCar()
# wc = WorkCar()
# pc = PoliceCar()


