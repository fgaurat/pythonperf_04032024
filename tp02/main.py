the_prefix = "THELOG"



def do_log(prefix=""):
    def wrapper_f(func):

        def wrapper(*args,**kwargs):
            print(prefix,"Log",func.__name__,*args,**kwargs)
            r = func(*args,**kwargs)
            print(prefix,"Log return ",func.__name__,r)
            return r
        
        return wrapper
    return wrapper_f


@do_log(the_prefix)
def say_hello(name):
    return f"Hello {name}"


def main():
    h = say_hello("fred")
    print(h)

if __name__=='__main__':
    main()
