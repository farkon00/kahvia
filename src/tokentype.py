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
    CHILD = auto() # :: - Get the child of a parent
    SET = auto() # = - Set a value to another
    INTEGER = auto()
    TYPEANNOTATION = auto() # : - mark the type of a variable or argument


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
        ',': TokenType.ARGSEPARATE,
        '=': TokenType.SET,
        ':': TokenType.TYPEANNOTATION
    }

    MULTI_SYMBOLS: Dict[str, TokenType] = {
        '->': TokenType.RETURNTYPE,
        '//': TokenType.COMMENT,
        '::': TokenType.CHILD
    }

    KEYWORDS: List[str] = ["proc", "void", "import", "const", "int"]
