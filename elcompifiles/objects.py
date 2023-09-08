from abc import(
    ABC, 
    abstractmethod
)
from enum import(
    auto,
    Enum
)

class ObjectType(Enum):
    BOOLEAN=auto()
    INTEGER=auto()
    NULL=auto()
    FLOAT=auto()
    STRING=auto()
    

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
    
