from enum import Enum

class TokenType(Enum):
    PRINT = 0
    INTLIT = 1
    VARREF = 2
    ASSIGN = 3
    PLUS = 4
    MINUS = 5
    TIMES = 6
    DIVIDE = 7
    LPAREN = 8
    RPAREN = 9
    EOF = 10



class Token:

    def __init__(
        self, 
        tokentype: TokenType, 
        lexeme: str,
        *,  
        name: str | None = None,
        intvalue: int | None = None,
    ):

        self.tokentype = tokentype
        self.lexeme = lexeme
        self.name = name
        self.intvalue = intvalue

    def __str__(self):
        namepart = f"; name: {self.name}" if self.name is not None else ""
        intvalpart = f"; intval: {str(self.intvalue)}" if self.intvalue is not None else ""

        return f"[Token type: {self.tokentype}; lexeme: {self.lexeme}{namepart}{intvalpart}]"


    
