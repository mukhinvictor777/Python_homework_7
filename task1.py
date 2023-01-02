"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:

    import time

    red_color_time = 7
    yellow_color_time = 2
    green_color_time = 5

    red_color = 'красный'
    yellow_color = 'желтый'
    green_color = 'зеленый'

    def __init__(self, color):
        self.__color = color

    def switch(self, color, light_time):
        self.light_time = light_time
        print(f'\nВключен {color} свет, до переключения {self.light_time} сек')
        time.sleep(self.light_time)

    def running(self, color=''):
        if not color:
            first_color = self.__color
        else:
            first_color = color

        if first_color == self.red_color:
            self.switch('красный', self.red_color_time)
            self.switch('желтый', self.yellow_color_time)
            self.switch('зеленый', self.green_color_time)
        elif first_color == self.yellow_color:
            self.switch('желтый', self.yellow_color_time)
            self.switch('зеленый', self.green_color_time)
            self.switch('красный', self.red_color_time)
        elif first_color == self.green_color:
            self.switch('зеленый', self.green_color_time)
            self.switch('красный', self.red_color_time)
            self.switch('желтый', self.yellow_color_time)
        else:
            print(f'Светофор содержит только 3 цвета: красный, желтый и зеленый')

        print("\nЦикл переключения светофора завершен")


trl_a = TrafficLight('красный')
trl_a.running()

trl_b = TrafficLight('')
trl_b.running('желтый')

