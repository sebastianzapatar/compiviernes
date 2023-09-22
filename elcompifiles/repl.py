from typing import List


from elcompifiles.lexer import Lexer
from elcompifiles.parser import Parser
from elcompifiles.ast import Program
from elcompifiles.evaluator import evaluate
from elcompifiles.tokens import(
    Token,
    TokenType
)
 
EOF_TOKEN:Token=Token(TokenType.EOF,'')
def star_repel()->None:
    scanned:List[str]=[]
    while(source:=input('>> '))!='salir()':
        scanned.append(source)
        lexer:Lexer=Lexer(' '.join(scanned))
        parser:Parser=Parser(lexer)
        program:Program=parser.parse_program()
        evaluated=evaluate(program)

        if(evaluated is not None):
            print(evaluated.inspect())

