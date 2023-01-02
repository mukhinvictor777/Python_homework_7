"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'\nТекущая скорость автомобиля {self.name}: {self.speed} км/ч')

    def show_parameters(self):
        print(f'\nМарка автомобиля: {self.name}')
        print(f'\nЦвет автомобиля: {self.color}')
        if self.is_police:
            print('\nАвтомобиль является полицейским')
        else:
            print('\nАвтомобиль явлется гражданским')
    def go(self):
        print(f'\nМашина {self.name} поехала со скоростью {self.speed}')

    def stop(self):
        print(f'\nМашина {self.name} остановилась')

    def turn(self, direction):
        print(f'\nМашина {self.name} повернула на{direction}')

class TownCar(Car):
    speed_limit = 60
    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'\nДопустимая скорость {self.speed_limit}'
                  f'\nВаша скорость равна {self.speed}'
                  f'\nВы двигаетесь  с превышением скорости {self.speed - self.speed_limit}')
        else:
            print(f'\nДопустимая скорость {self.speed_limit}'
                  f'\nВаша скорость равна {self.speed}')


class SportCar(Car):
    speed_limit = 200


class WorkCar(Car):
    speed_limit = 40
    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'\nДопустимая скорость {self.speed_limit}'
                  f'\nВаша скорость равна {self.speed}'
                  f'\nВы двигаетесь  с превышением скорости {self.speed - self.speed_limit}')
        else:
            print(f'\nДопустимая скорость {self.speed_limit}'
                  f'\nВаша скорость равна {self.speed}')


class PoliceCar(Car):
    speed_limit = 200

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


my_car = TownCar(70, 'белый', 'Mercedes S500', False)
my_car.show_parameters()
my_car.go()
my_car.show_speed()
my_car.turn('право')
my_car.stop()

work_car = WorkCar(50, 'черный', 'Toyota Camry', False)
work_car.show_parameters()
work_car.go()
work_car.turn('лево')
work_car.show_speed()
work_car.stop()

police = PoliceCar(80, 'синий', 'Ваз 2110', False)
police.show_parameters()
