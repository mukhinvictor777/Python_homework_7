"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна
Использовать формулу: длина ширина масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:

    thickness = 5
    weight = 25

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def asphalt_weight(self, length, width):
        if not length:
            length = self.__length
        if not width:
            width = self.__width
        asphalt_weight = int(length) * int(width) * self.weight * self.thickness
        print(f'\nМасса асфальта для покрытия дорожного полотна длиной {length} метров и шириной {width} метров ' 
              f'равна {asphalt_weight//1000} т')


example_road = Road('5000', '20')
example_road.asphalt_weight('', '')
example_road.asphalt_weight(10000, 50)




