from dataclasses import dataclass

@dataclass
class Customer:
    id:int=0
    first_name:str=""
    last_name:str=""
    email:str=""
    gender:str=""
    ip_address:str=""
