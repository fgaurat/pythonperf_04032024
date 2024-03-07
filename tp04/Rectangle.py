

class Rectangle:

    __cpt = 0

    __slots__ = ("__longueur","__largeur")
    def __init__(self,longueur=0,largeur=0):
        self.__longueur =longueur
        self.__largeur = largeur
        Rectangle.__cpt+=1
    
    
    @classmethod
    def buildFromStr(cls,value):
        params = [int(i) for i in value.split(',')] # [int('12'),int('4')] = [12,4]
        return cls(*params)

    @property
    def longueur(self):
        return self.__longueur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @longueur.setter
    def longueur(self,longueur):
        self.__longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        self.__largeur = largeur
    
    @property
    def surface(self):
        return self.__longueur*self.__largeur

    def __str__(self):
        return f"{__class__.__name__} {self.__longueur=}, {self.__largeur=}"


    def __eq__(self, o)->bool:
        return self.__longueur == o.__longueur and  self.__largeur == o.__largeur
    
    
    @staticmethod
    def get_cpt():
        return Rectangle.__cpt
    # longueur = property(get_longueur,set_longueur,None,"propriété longueur")
    # largeur = property(get_largeur,set_largeur,None,"propriété largeur")