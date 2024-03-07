from Rectangle import Rectangle


def main():
    r = Rectangle()
    r1 = Rectangle()
    print(r,hex(id(r)))
    print(r1,hex(id(r1)))
    print(type(Rectangle))
if __name__=='__main__':
    main()
