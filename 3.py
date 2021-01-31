class Worker:
    # def __init__(self, name, surname, pos):
    #     self.name = name
    #     self.surname = surname
    #     self.pos = pos
    _income = {"wage": 0, "bonus": 0}

class Position(Worker):
    def get_full_name(self):
        print('Полное имя сотрудника: ', name, surname, 'Должность: ', pos)

    def get_total_income(self):
        print('Доход с учетом премии: ', wage + bonus)

p = Position()

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
pos = input('Должность: ')
wage = float(input('Введите оклад: '))
bonus = float(input('Введите премию: '))

p.get_full_name()
p.get_total_income()
