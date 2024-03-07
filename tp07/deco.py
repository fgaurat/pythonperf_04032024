def singleton(cls):
    instances = {}
    c = 2

    def wrapper(*args, **kwargs):
        global inst
        print("wrapper singleton", args, kwargs,inst)
        if not inst:
            inst = 4
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Test:

    def __init__(self):
        print("test")



def main():
    t =Test()

if __name__=='__main__':
    main()
