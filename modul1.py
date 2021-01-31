class Auto:

    count = 0

    def __init__(self, color, speed):
        self.my_color = color
        self.my_speed = speed
        self.status = 'stop'
        Auto.count += 1

    def start(self):
        self.status = 'start'
    def stop(self):
        self.status = 'stop'

zaz = Auto('blue', 50)
ferarri = Auto('red', 320)

print(zaz.status)
print(ferarri.status)
zaz.start()
print(zaz.status)
print(ferarri.status)
