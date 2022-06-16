from enum import Enum

class Token():
    def __init__(typ, val=''):
        self.typ = typ
        self.val = val

class TokenType(Enum):
    IDENTIFIER = 0
