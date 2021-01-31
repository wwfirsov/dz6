import time

class TrafficLight:
    __color = 0

    def running(self):
        # while color == 0:
            self.light_green = "Зеленый"
            self.light_yellow = "Желтый"
            self.light_red = "Красный"
            print(self.light_green)
            time.sleep(5)
            print(self.light_yellow)
            time.sleep(2)
            print(self.light_red)
            time.sleep(5)

a = TrafficLight()
a.running()


