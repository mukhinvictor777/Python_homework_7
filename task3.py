"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def __init__(self, worker, income):
        self.__income = income
        self.name = worker.name
        self.surname = worker.surname
        self.position = worker.position

    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return full_name

    def get_total_income(self):
        total_income = self.__income['wage'] + self.__income['bonus']
        print(f'\nЗаработанная плата сотрудника {self.get_full_name()} с учетом премии составляет {total_income} руб.')


worker_a = Worker('Viktor', 'Mukhin', 'intern')
position_a = Position(worker_a, {'wage': 50000, 'bonus': 20000})
print(f'\nПолное имя сотрудника: {position_a.get_full_name()}')
position_a.get_total_income()
