import multiprocessing
import time


def countdown():
     x = 10000000
     while x > 0:
           x -= 1
# Implementation 1: Multi-threading

def implementation_1():

     thread_1 = multiprocessing.Process(target=countdown)
     thread_2 = multiprocessing.Process(target=countdown)
     thread_3 = multiprocessing.Process(target=countdown)
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


if __name__ == '__main__':
    start = time.perf_counter()
    implementation_1()
    finish = time.perf_counter()
    print(F"Multiprocessing Finished in {round(finish-start,3)} seconds")

    start = time.perf_counter()
    implementation_2()
    finish = time.perf_counter()
    print(F"Sequential Finished in {round(finish-start,3)} seconds")