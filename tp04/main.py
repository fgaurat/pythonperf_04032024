from Rectangle import Rectangle
from DataRectangle import DataRectangle

def main():
    r = Rectangle(1,2)
    print(r.longueur)
    r.longueur = 12
    r.largeur = 2
    print(r.surface)

    s = str(r)
    print(s)
    r1 = Rectangle(1,2)
    r2 = Rectangle(1,2)
    if r1 == r2:
        print("ok")
    else:
        print("ko")
    
    # r1.toto="hello"
    print(r1.__slots__)
    print("Rectangle.cpt",Rectangle.get_cpt())
    print(r1.get_cpt())

    r3 = Rectangle.buildFromStr("12,4")
    print(r3)


    print(50*"-")
    rd = DataRectangle(5,8)
    print(rd.largeur,rd.longueur)
    print(rd)
if __name__=='__main__':
    main()
