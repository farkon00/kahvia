from enum import Enum, auto, unique
from typing import Dict, List

@unique
class TokenType(Enum):
    IDENTIFIER = auto() # An identifier such as a variable or procedure name
    ENDOFLINE = auto() # ;
    RETURNTYPE = auto() # -> - Indicates the return type of a procedure
    KEYWORD = auto() # A reserved keyword
    COMMENT = auto() # //
    OPENBRACKET = auto() # (, [, {
    CLOSEBRACKET = auto() # ), ], }
    ARGSEPARATE = auto() # , - Separates arguments in a procedure call/definition
    STRINGLITERAL = auto() # A string literal

class Token():
    def __init__(self, typ: TokenType, val: str=''):
        self.typ: TokenType = typ
        self.val: str = val

class TokenRef():
    SINGLE_SYMBOLS: Dict[str, TokenType] = {
        ';': TokenType.ENDOFLINE,
        '{': TokenType.OPENBRACKET,
        '}': TokenType.CLOSEBRACKET,
        '(': TokenType.OPENBRACKET,
        ')': TokenType.CLOSEBRACKET,
        '[': TokenType.OPENBRACKET,
        ']': TokenType.CLOSEBRACKET,
        ',': TokenType.ARGSEPARATE
    }

    MULTI_SYMBOLS: Dict[str, TokenType] = {
        '->': TokenType.RETURNTYPE,
        '//': TokenType.COMMENT
    }

    KEYWORDS: List[str] = ["proc", "printfs", "void"]
