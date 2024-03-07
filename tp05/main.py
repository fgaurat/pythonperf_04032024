from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle


def main():
    r = Rectangle(2,3)
    c = Carre(2)
    print(c)
    print(c.surface)
    c.cote = 12
    print(c.surface)
    print(r.surface)

    ce = Cercle(2)
    print(ce.surface)
    


if __name__=='__main__':
    main()
