"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:

    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f'\nЗапуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'\nВы выбрали канцелярский предмет: {self.name}'
              f'\nЗапуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print(f'\nВы выбрали канцелярский предмет: {self.name}'
              f'\nЗапуск отрисовки')


class Handle(Stationery):
    def draw(self):
        print(f'\nВы выбрали канцелярский предмет: {self.name}'
              f'\nЗапуск отрисовки')


a = Stationery('')
a.draw()

b = Pen('Ручка')
e = Pencil('Карандаш')
d = Handle('Маркер')

b.draw()
e.draw()
d.draw()
