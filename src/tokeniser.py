import kahvia
import re
from src.tokentype import Token, TokenType, TokenRef
from typing import Iterable, List, Tuple

""" 
Tokeniser
"""

class Tokeniser:
    """
    Tokeniser Class
    """

    def __init__(self, f_path: str):
        self.col = self.row = self.char = 0
        self.file_path = f_path

    def exists_starts_with(self, arr: Iterable, to_search: str, ignore_exact_match: bool = True) -> bool:
        for to_check in arr:
            if to_check.startswith(to_search):
                if ignore_exact_match and not to_check == to_search:
                    return True
                elif not ignore_exact_match:
                    return True
        return False

    def get_current_loc(self) -> str:
        return f"{self.file_path}:{self.row}:{self.col}"

    def get_next_token(self, current_line: str) -> Tuple[str, Token]:
        current_token: str = ""

        next_token: Token | None = None
        in_string: bool = False

        for i, c in enumerate(current_line):
            self.col += 1
            self.char += 1
            if (c.isspace() or c == "\n") and not in_string:
                continue
            current_token += c
            if c == '"':
                # String teim!
                if not in_string:
                    in_string = True
                else:
                    in_string = False
                    next_token = Token(TokenType.STRINGLITERAL, current_token)
                    current_token = ""

            if in_string:
                continue

            if current_token in TokenRef.SINGLE_SYMBOLS:
                if not self.exists_starts_with(TokenRef.MULTI_SYMBOLS, current_token) or i == len(current_line) - 1:
                    next_token = Token(TokenRef.SINGLE_SYMBOLS[current_token], current_token)
                    current_token = ""
                else:
                    if not self.exists_starts_with(TokenRef.MULTI_SYMBOLS, current_token + current_line[i + 1], False):
                        next_token = Token(TokenRef.SINGLE_SYMBOLS[current_token], current_token)
                        current_token = ""
            elif self.exists_starts_with(TokenRef.MULTI_SYMBOLS, current_token, False):
                if current_token in TokenRef.MULTI_SYMBOLS and not i == len(current_line) - 1:
                    if not self.exists_starts_with(TokenRef.MULTI_SYMBOLS, current_token + current_line[i + 1], False):
                        next_token = Token(TokenRef.MULTI_SYMBOLS[current_token], current_token)
                        current_token = ""
            elif self.exists_starts_with(TokenRef.KEYWORDS, current_token, False):
                if current_token in TokenRef.KEYWORDS and not i == len(current_line) - 1:
                    if current_line[i + 1].isspace() or not current_line[i + 1].isalpha():
                        next_token = Token(TokenType.KEYWORD, current_token)
                        current_token = ""
                elif current_token in TokenRef.KEYWORDS:
                    next_token = Token(TokenType.KEYWORD, current_token)
            elif bool(re.search("^[A-Za-z_]+$", current_token)):
                if i == len(current_line) - 1:
                    next_token = Token(TokenType.IDENTIFIER, current_token)
                elif not (current_line[i + 1].isalpha() or current_line[i + 1] == '_'):
                    next_token = Token(TokenType.IDENTIFIER, current_token)
            elif current_token.isnumeric():
                if i == len(current_line) - 1:
                    next_token = Token(TokenType.INTEGER, current_token)
                elif not current_line[i + 1].isnumeric():
                    next_token = Token(TokenType.INTEGER, current_token)
            else:
                kahvia.error(f"Unexpected token: {c} at {self.get_current_loc()}", False)

            if next_token is not None:
                return current_line[i + 1:], next_token

    def tokenise_line(self, line: str) -> List[Token]:
        self.row += 1
        self.col = 0
        line_tokens: List[Token] = []
        while line.strip():
            next_tok: Token
            line, next_tok = self.get_next_token(line)
            line_tokens.append(next_tok)
        return line_tokens

    def tokenise_file(self) -> List[Token]:
        file_contents: List[str] = []
        tokens: List[Token] = []
        try:
            with open(self.file_path, 'r') as f:
                file_contents = f.readlines()
        except FileNotFoundError:
            kahvia.error(f"The file `{self.file_path}` could not be found", False)
        except PermissionError:
            kahvia.error(f"Your user does not have permission to read the file `{self.file_path}`", False)
        except ValueError:
            kahvia.error(f"There was an error reading the encoding of the file `{self.file_path}`", False)
        except Exception:
            kahvia.error(f"Unknown error reading the file `{self.file_path}`", False)

        for line in file_contents:
            if not line:
                continue
            tokens.extend(self.tokenise_line(line))

        return tokens
