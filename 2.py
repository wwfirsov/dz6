class Road:

    _length = 20
    _width = 5000

    def asfalt(self, mass, tol):
        self.mass = mass
        self.t = tol
        polotno = r._width * r._length * mass * tol
        print('Масса асфальта: ', polotno, ' тонн')

r = Road()
mass = int(input('Введите массу: '))
tol = int(input('Введите толщину: '))
r.asfalt(mass, tol)







