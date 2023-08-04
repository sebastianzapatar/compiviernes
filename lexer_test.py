from unittest import TestCase
from typing import List
from elcompifiles.tokens import(
    Token,
    TokenType
)
from elcompifiles.lexer import(
    Lexer
)
class TestTokens(TestCase):
    def test_ilegal(self)->None:
        source:str='!¿@'
        lexer:Lexer=Lexer(source)
        tokens:List[Token]=[]
        for i in range(len(source)):
            tokens.append(lexer.next_token())
        expected_tokens:List[Token]=[
            Token(TokenType.ILLEGAL,'!'),
            Token(TokenType.ILLEGAL,'¿'),
            Token(TokenType.ILLEGAL,'@'),
        ]
        self.assertEqual(expected_tokens,tokens)
