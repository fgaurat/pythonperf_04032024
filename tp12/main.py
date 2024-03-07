import timeit
import os
import threading

def init_loop():
    r = []
    for i in range(100):
        r.append(i)

def init_map():
    r = list(map(lambda i:i,range(100)))

def init_comp():
    r = [i for i in range(100)]    
    

def main():

    t1 = timeit.timeit("init_loop()",setup="from __main__ import init_loop",number=2)
    t1 = timeit.timeit(init_loop)
    # t2 = timeit.timeit("init_map()",setup="from __main__ import init_map")
    # t3= timeit.timeit("init_comp()",setup="from __main__ import init_comp")
    print("init_loop",t1)
    print("init_map",t2)
    print("init_comp",t3)
    print(threading.current_thread().name)

if __name__=='__main__':
    main()
