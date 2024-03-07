class TheClass:

    def __new__(cls):
        print("def __new__(self)")
        return super(TheClass,cls).__new__(cls)

    def __init__(self):
        print("def __init__(self)")
        self.v = "value"


    def __call__(self):
        print("__call__")

def main01():
    t = TheClass()
    t()



def main():
    r = Rectangle()
if __name__=='__main__':
    main()
