from enum import Enum

class Token():
    def __init__(self, typ: TokenType, val: str=''):
        self.typ: TokenType = typ
        self.val: str = val

class TokenType(Enum):
    IDENTIFIER = 0
