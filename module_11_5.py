# Многопроцессное программированиех#module_11_5.py
##Задача "Многопроцессное считывание":
import time
import threading
import random
from platform import release
import multiprocessing
def read_info(name):
    all_data= []
    file = open(name, 'r')
    line = file.readline()
    all_data.append(line)
    while line:
        line = file.readline()
        all_data.append(line)
    file.close()
#filenames = [f'./file {number}.txt' for number in range(1, 5)]
#print(filenames)
#ntime=time.time()
#read_info('file 1.txt')
#read_info('file 2.txt')
#read_info('file 3.txt')
#read_info('file 4.txt')
#ktime=time.time()
#print(f'линейный {ktime-ntime}')
ntime=time.time()
if __name__ == '__main__':
    pr1=multiprocessing.Process(target=read_info, args=('file 1.txt',))
    pr2=multiprocessing.Process(target=read_info, args=('file 2.txt',))
    pr3=multiprocessing.Process(target=read_info, args=('file 3.txt',))
    pr4=multiprocessing.Process(target=read_info, args=('file 4.txt',))
    pr1.start()
    pr2.start()
    pr3.start()
    pr4.start()
multiprocessing.cpu_count()
ktime=time.time()
print(f'многопроцессный {ktime-ntime}')
