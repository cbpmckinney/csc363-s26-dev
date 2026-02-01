from tokens import *

class TokenStream:
    
    def __init__(self):
        self.tokens: list[Token] = []
        self.pos = 0

    def append(self, token: Token) -> None:
        self.tokens.append(token)

    def __iter__(self):
        return iter(self.tokens)
    
    def __len__(self):
        return len(self.tokens)
    
    def eots(self) -> bool:
        return self.pos >= self.__len__()

    def advance(self):
        self.pos += 1

    def read(self) -> Token:
        tok = self.tokens[self.pos]
        self.advance()
        return tok
    
    def peek(self) -> Token:
        return self.tokens[self.pos]
    
