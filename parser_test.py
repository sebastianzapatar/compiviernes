from unittest import TestCase

from elcompifiles.ast import Program
from elcompifiles.lexer import Lexer
from elcompifiles.parser import Parser
from typing import (
    cast,
    List,
)
from elcompifiles.ast import (
    Identifier,
    LetStatement,
    Statement,
    Expression,
    Program,
    ReturnStatement
    
)
class ParserTest(TestCase):

    def test_parse_program(self) -> None:
        source: str = 'variable x =5;'
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertIsNotNone(program)
        self.assertIsInstance(program, Program)
    def test_let_statements(self) -> None:
        source: str = '''
            variable x = 5;
            variable y = 10;
            variable foo = 20;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        self.assertEqual(len(program.statements), 3)

        for statement in program.statements:
            self.assertEqual(statement.token_literal(), 'variable')
            self.assertIsInstance(statement, LetStatement)

    def test_names_in_let_statements(self) -> None:
        source: str = '''
            variable x = 5;
            variable y = 10;
            variable foo = 20;
        '''
        lexer: Lexer = Lexer(source)
        parser: Parser = Parser(lexer)

        program: Program = parser.parse_program()

        names: List[str] = []
        for statement in program.statements:
            statement = cast(LetStatement, statement)
            assert statement.name is not None
            names.append(statement.name.value)

        expected_names: List[str] = ['x', 'y', 'foo']

        self.assertEquals(names, expected_names)
    
    def test_parse_errors(self)-> None:
        source:str='variable x 5;'
        lexer:Lexer=Lexer(source)
        parser:Parser=Parser(lexer)
        program:Program=parser.parse_program()

        self.assertEqual(len(parser.errors),1)

    def test_return_statament(self)-> None:
        source:str=''' 
            regresa 5;
            regresa foo;
        '''
        lexer:Lexer=Lexer(source)
        parser:Parser=Parser(lexer)
        program:Program=parser.parse_program()

        self.assertEqual(len(program.statements),2)

        for statemen in program.statements:
            self.assertEqual(statemen.token_literal(),'regresa')
            self.assertIsInstance(statemen,ReturnStatement)
