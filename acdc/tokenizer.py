from charstream import CharStream
from tokens import Token, TokenType
from tokenstream import TokenStream

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

        # To do: based on this char, decide what to do next
        # We can handle some of this with a match
        # Others require a conditional (because of more complex logic)
        match char:

            case '=':
                return Token(TokenType.ASSIGN, lexeme = '=')
            
            case '(':
                raise NotImplementedError
                
            case ')': 
                raise NotImplementedError
            
            case '+' | '-' | '*' | '/' | '^':
                raise NotImplementedError
            
            case 'i':
                # Todo: peek next character, validate 
                # Create and return appropriate token
                # Note: you already have the char 'i', so don't lose it
                raise NotImplementedError

            case 'p':
                # Todo: peek next character, validate
                # Create and return appropriate token
                raise NotImplementedError
            
            case _:
                pass # Move on to secondary inspection

        if char.isdigit():
            # Todo: finish reading integer literal using readintliteral(char)
            # Create and return appropriate token
            # Note: char already has the first digit, so don't lose it.
            raise NotImplementedError    

        if char.isalpha():
            # Todo: make sure char is a valid variable
            # 
            raise NotImplementedError
        

        raise ValueError(f"Unexpected character: {char}")
        
    

    def readintliteral(self, firstchar: str) -> tuple[str, int]:
        
        digits: list[str] = []
        digits.append(firstchar)
        while not self.cs.eof() and self.cs.peek().isdigit():
            digits.append(self.cs.read())

        lexeme = ''.join(digits)

        return lexeme, int(lexeme)

