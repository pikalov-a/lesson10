# Потоки на классах#module_10_3.py
##Задача "За честь и отвагу!":
import time
import threading
import random
from platform import release


class Bank(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance=0
        self.lock=threading.Lock()
    def run(self):
        self.deposit(self.balance, self.lock)
        self.take(self.balance, self.lock)

    def deposit(self):
        for i in range(100):
            xplus=random.randint(50,500)
            self.balance += xplus
            print(f'++{i}Пополнение: {xplus}.Баланс: {self.balance}')
            time.sleep(0.001)
            if self.lock.locked() and self.balance>=500:
                self.lock.release()
    def take(self):
        for i in range(100):
            xminus=random.randint(50,500)
            time.sleep(0.001)
            if self.balance>xminus:
                self.balance -= xminus
                print(f'--{i}   Снятие {xminus}.Баланс: {self.balance}')
            else:
                print(f'--{i}   Попытка снятия {xminus}.Баланс: {self.balance}')
                print('Запрос отклонён, недостаточно средств')

                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')
