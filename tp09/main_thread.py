import threading


the_lock = threading.Lock()

def tl1():
    with the_lock:
        for i in range(5):
            print(threading.current_thread().name,i)

def tl2():
    with the_lock:
        for i in range(5):
            print(threading.current_thread().name,i)

def main():
    th1 = threading.Thread(target=tl1)
    th2 = threading.Thread(target=tl2)
    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print("la fin")


if __name__=='__main__':
    main()
