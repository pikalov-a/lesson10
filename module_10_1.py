# Создание потоков#module_10_1.py
##Задача "Потоковая запись в файлы":
import threading
#from time import sleep
#from time import time
import time
import threading
def write_words(word_count, file_name):
    my_file = open(file_name, "w+", encoding='utf-8')
    for i in range(word_count):
        my_file.write(f"Какое-то слово № {i+1}" )
        my_file.write('\n')
        time.sleep(0.1)
    my_file.close()
    print(f'Завершилась запись в файл {file_name}')
ntime=time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ktime=time.time()
print(f'Работа потоков {ktime-ntime}')
ntime=time.time()
thread5=threading.Thread(target=write_words,args=(10, 'example5.txt')) ##3 аргумент ,daemon=True выполняется фоново, не до конца (до конца других явных процессов)
thread6=threading.Thread(target=write_words,args=(30, 'example6.txt')) ## 3 аргумент не работает
thread7=threading.Thread(target=write_words,args=(200, 'example7.txt'))
thread8=threading.Thread(target=write_words,args=(100, 'example8.txt'))
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
ktime=time.time()
print(f'Работа потоков {ktime-ntime}')
##xn=my_file.tell()
