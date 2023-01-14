import multiprocessing
import threading
import time
import os

def hello_threading(s):
    print('Function start! ', s, 'pid:', os.getpid(), 'thread id:', threading.get_ident())
    time.sleep(1)
    
t1 = threading.Thread(target=hello_threading, args=['Hello World'])
t2 = threading.Thread(target=hello_threading, args=['Hello Chris'])

t1.start()
t2.start()

t1.join()
t2.join()


def hello(s):
    print('Function start! ', s, 'pid:', os.getpid(), 'thread id:', threading.get_ident())
    time.sleep(1)
    
p1 = multiprocessing.Process(target=hello, args=['Hello World'])
p2 = multiprocessing.Process(target=hello, args=['Hello Chirs'])

p1.start()
p2.start()

p1.join()
p2.join()