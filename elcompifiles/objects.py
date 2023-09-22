from abc import(
    ABC, 
    abstractmethod
)
from enum import(
    auto,
    Enum
)
from typing import Dict



class ObjectType(Enum):
    BOOLEAN=auto()
    INTEGER=auto()
    NULL=auto()
    FLOAT=auto()
    STRING=auto()
    RETURN=auto()
    

class Object(ABC):
    @abstractmethod
    def type(self)->ObjectType:
        pass

    @abstractmethod
    def inspect(self)->str:
        pass

class Integer(Object):
    def __init__(self,value:int) -> None:
        self.value=value
    
    def type(self)->ObjectType:
        return ObjectType.INTEGER
    
    def inspect(self) -> str:
        return str(self.value)

class Boolean(Object):
    def __init__(self,value:bool) -> None:
        self.value=value
    
    def type(self)->ObjectType:
        return ObjectType.BOOLEAN
    
    def inspect(self) -> str:
        return str(self.value)

class Null(Object):
    
    
    def type(self)->ObjectType:
        return ObjectType.NULL
    
    def inspect(self) -> str:
        return 'nulo'
    
class Return(Object):
    def __init__(self,value:Object) -> None:
        self.value=value
    
    def type(self)->ObjectType:
        return ObjectType.RETURN
    
    def inspect(self) -> str:
        return self.value.inspect()
"""
Esta clase es la que se va a utilizar para guardar
Las variables
"""
class Enviroment(Dict):
    #El store es un diccionario por defecto
    def __init__(self):
        self._store = dict()
    def __getitem__(self, __key):
        return self._store[__key]
    def __setitem__(self, __key, __value):
        self._store[__key]=__value
    def __delitem__(self, __key):
        del self._store[__key]