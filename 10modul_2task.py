"""Домашнее задание по теме "Потоки на классах"""

from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        all_enemies = 100
        rem_enemies = all_enemies
        print(f'{self.name}, на нас напали!')
        for i in range(1, all_enemies // self.power + 1):
            rem_enemies -= self.power
            sleep(1)
            print(f'{self.name} сражается {i} день(дня), осталось {rem_enemies} воинов.')
        print(f'{self.name} одержал победу спустя {all_enemies // self.power} дней(дня)!')


#Пример результата выполнения программы:
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')

