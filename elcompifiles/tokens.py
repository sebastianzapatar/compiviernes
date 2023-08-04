from enum import(
    auto,
    Enum,
    unique
)
from typing import (
    NamedTuple,
    Dict
)
@unique
class TokenType(Enum):
    ASSING=auto()
    COMMA=auto()
    ELSE=auto()
    EOF = auto()
    FUNCTION=auto()
    IDENTIFIER=auto()
    IF=auto()
    GT=auto()
    GTE=auto()
    ILLEGAL=auto()
    INTEGER=auto()
    LBRACE=auto()
    LET=auto()
    LPAREN=auto()
    LT=auto()
    LTE=auto()
    MINUS=auto()
    PLUS=auto()
    RBRACE=auto()
    RPAREN=auto()
    SEMICOLON=auto()


class Token(NamedTuple):
    token_type:TokenType
    literal:str
    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal {self.literal}'
def lookup_token_type(literal:str)->TokenType:
    keywords:Dict[str,TokenType]={
        'funcion':TokenType.FUNCTION,
        'variable':TokenType.LET,
        'si':TokenType.IF,
        'si_no':TokenType.ELSE
    }
    return keywords.get(literal,TokenType.IDENTIFIER)