from multiprocessing import Pool
import os
import time

def f(x):
    start = time.time()
    t = 1
    while time.time()-start < t:
        pass
    return x*x

def main():
    print(os.cpu_count())
    with Pool(3) as p:
        print(p.map(f, range(30)))

if __name__=='__main__':
    main()
