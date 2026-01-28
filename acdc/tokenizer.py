from charstream import CharStream
from tokens import Token, TokenType
from tokenstream import TokenStream
import string

RESERVED = {'i', 'f', 'o', 'n', 'p'}
VALID_VARS = set(string.ascii_lowercase) - RESERVED

class Tokenizer:

    def __init__(self, cs: CharStream):
        self.cs = cs

    def tokenize(self) -> TokenStream:
        ts = TokenStream()
        while not self.cs.eof():
            tok = self.nexttoken()
            ts.append(tok)

        ts.append(Token(TokenType.EOF, lexeme = ''))
        return ts
    

    def nexttoken(self) -> Token:

        char = self.cs.read()
        while char in {' ', '\n', '\r', '\t'}:
            char = self.cs.read() # Consume chars for space, newline, etc.

        # To do: based on this char, decide what to do next
        # We can handle some of this with a match
        # Others require a conditional (because of more complex logic)
        match char:

            case '=':
                return Token(TokenType.ASSIGN, lexeme = f"{char}")
            
            case '(':
                return Token(TokenType.LPAREN, lexeme = f"{char}")
                
            case ')': 
                return Token(TokenType.RPAREN, lexeme = f"{char}")
            
            case '+':
                return Token(TokenType.PLUS, lexeme = f"{char}")
            case '-':
                return Token(TokenType.MINUS, lexeme = f"{char}")
            case '*':
                return Token(TokenType.TIMES, lexeme = f"{char}")
            case '/':
                return Token(TokenType.DIVIDE, lexeme = f"{char}")
            case '^':
                return Token(TokenType.EXPONENT, lexeme = f"{char}")
            
            case 'i':
                nextchar = self.cs.peek()
                if nextchar not in VALID_VARS:
                    raise ValueError(f"Invalid variable character: {nextchar}")
                else:
                    self.cs.advance()
                    return Token(TokenType.INTDEC, lexeme = f"{char}{nextchar}")

            case 'p':
                nextchar = self.cs.peek()
                if nextchar not in VALID_VARS:
                    raise ValueError(f"Invalid variable character: {nextchar}")
                else:
                    self.cs.advance()
                    return Token(TokenType.PRINT, lexeme = f"{char}{nextchar}")
                
            case _:
                pass # Move on to secondary inspection

        if char.isdigit():
            lexeme, intvalue = self.readintliteral(char)
            return Token(TokenType.INTLIT, lexeme = lexeme, intvalue = intvalue)

        if char.isalpha():
            if char not in VALID_VARS:
                raise ValueError(f"Invalid variable character: {char}")
            else:
                return Token(TokenType.VARREF, lexeme = f"{char}")
           
        

        raise ValueError(f"Unexpected character: {char}")
        
    

    def readintliteral(self, firstchar: str) -> tuple[str, int]:
        
        digits: list[str] = []
        digits.append(firstchar)
        while not self.cs.eof() and self.cs.peek().isdigit():
            digits.append(self.cs.read())

        lexeme = ''.join(digits)

        return lexeme, int(lexeme)

