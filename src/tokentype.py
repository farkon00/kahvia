from enum import Enum

class TokenType(Enum):
    IDENTIFIER = 0

class Token():
    def __init__(self, typ: TokenType, val: str=''):
        self.typ: TokenType = typ
        self.val: str = val
