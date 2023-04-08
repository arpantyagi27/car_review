from threading import *
import time
def print_time(tname,counter, delay):
    for i in range (counter):
        time.sleep(delay)
        print("%s  %s "%(tname,time.ctime(time.time())))
t1=Thread(target=print_time,args=("t1",5,4))
t2=Thread(target=print_time,args=("t2",2,2))