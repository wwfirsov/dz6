class Stationery:
    title = "Название"

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Ручка')

class Pencil(Stationery):
    def draw(self):
        print('Карандаш')

class Handle(Stationery):
    def draw(self):
        print('Маркер')

p = Pen()
p.draw()

pl = Pencil()
pl.draw()

h = Handle()
h.draw()



