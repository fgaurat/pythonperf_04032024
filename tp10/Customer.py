from dataclasses import dataclass
class Customer:
    
    def __init__(self, 
        id:int = 0 , 
        first_name:str = '', 
        last_name:str = '', 
        email:str = '', 
        gender:str = '', 
        ip_address:str = ''
    ) -> None:
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gender = gender
        self.__ip_address = ip_address
    @property
    def id(self):
        return self.__id
    @property
    def first_name(self):
        return self.__first_name
    @property
    def last_name(self):
        return self.__last_name
    @property
    def email(self):
        return self.__email
    @property
    def gender(self):
        return self.__gender
    @property
    def ip_address(self):
        return self.__ip_address
        
    def __str__(self) -> str:

        return f"{__class__.__name__}({self.__id=},{self.__first_name=}, {self.__last_name=}, {self.__email=}, {self.__gender=}, {self.__ip_address=})"
        
