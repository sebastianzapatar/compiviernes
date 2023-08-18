from unittest import TestCase

from elcompifiles.ast import Program
from elcompifiles.lexer import Lexer
from elcompifiles.parser import Parser


class ParserTest(TestCase):

    def test_parse_program(self) -> None:
        source: str = 'variable x =5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)
        program: Program = parser.parse_program()
        self.assertIsNotNone(program)
        self.assertIsInstance(program, Program)