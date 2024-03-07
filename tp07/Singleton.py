


class Singleton(type):
    instance = None       # Attribut statique de classe
    def __call__(cls,*args,**kwargs): 
        "méthode de construction standard en Python"
        
        if cls.instance is None:
            cls.instance = super(Singleton,cls).__call__(*args,**kwargs)
        return cls.instance



        Rectangle(2,3)