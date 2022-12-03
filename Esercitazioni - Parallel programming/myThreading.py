#Esempio di multi-threading che, per via del GIL (Global Interpreter Lock)
# non implementa un vero parallel processing, per questo occorre usare multiprocessing

import threading
import time


def countdown():
     x = 10000000
     while x > 0:
           x -= 1
# Implementation 1: Multi-threading


def implementation_1():
     thread_1 = threading.Thread(target=countdown)
     thread_2 = threading.Thread(target=countdown)
     thread_3 = threading.Thread(target=countdown)
     thread_1.start()
     thread_2.start()
     thread_3.start()
     thread_1.join()
     thread_2.join()
     thread_3.join()

# Implementation 2: Run in serial
def implementation_2():
     countdown()
     countdown()
     countdown()



start = time.perf_counter()
implementation_1()
finish = time.perf_counter()
print(F"Imp1 Finished in {round(finish-start,3)} seconds")


start = time.perf_counter()
implementation_2()
finish = time.perf_counter()
print(F"Imp2 Finished in {round(finish-start,3)} seconds")