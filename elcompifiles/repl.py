from elcompifiles.lexer import Lexer
from elcompifiles.tokens import(
    Token,
    TokenType
)
EOF_TOKEN:Token=Token(TokenType.EOF,'')
def star_repel()->None:
    while(source:=input('>> '))!='salir()':
        lexer:Lexer=Lexer(source)

        while(token:=lexer.next_token())!=EOF_TOKEN:
            print(token)
