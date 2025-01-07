# Потоки на классах#module_10_2.py
##Задача "За честь и отвагу!":
import time
import threading
class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name=name
        self.power=power
    def war(self, name, power):
        delay = 1
        kolvrag = 100
        i = 0
        while kolvrag:
            i += 1
            kolvrag -= power
            time.sleep(delay)
            print(f'{name}, сражается {i} день(дня)..., осталось {kolvrag} воинов.')
        print(f'{name} одержал победу спустя {i} дней(дня)!')
    def run(self):
        print(f'{self.name}, на нас напали!')
        self.war(self.name,self.power)
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
