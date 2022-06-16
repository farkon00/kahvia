import kahvia
from src.tokentype import Token, TokenType, TokenRef
from typing import List, Tuple

# Tokeniser

col = row = char = 0

def exists_starts_with(arr, to_search: str, ignore_exact_match: bool=True):
    for to_check in arr:
        if to_check.startswith(to_search):
            if ignore_exact_match and not to_check == to_search:
                return True
            elif not ignore_exact_match:
                return True
    return False

def get_next_token(current_line: str) -> Tuple[str, Token]:
    global col, char, row
    current_token: str = ""
    col = 0
    next_token: Token = None
    in_string: bool = False
    
    for (i, c) in enumerate(current_line):
        col += 1
        char += 1
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
            if not exists_starts_with(TokenRef.MULTI_SYMBOLS, current_token) or i == len(current_line) - 1:
                next_token = Token(TokenRef.SINGLE_SYMBOLS[current_token], current_token)
                current_token = ""
            else:
                if not exists_starts_with(TokenRef.MULTI_SYMBOLS, current_token + current_line[i + 1], False):
                    next_token = Token(TokenRef.SINGLE_SYMBOLS[current_token], current_token)
                    current_token = ""
        elif exists_starts_with(TokenRef.MULTI_SYMBOLS, current_token, False):
            if current_token in TokenRef.MULTI_SYMBOLS and not i == len(current_line) - 1:
                if not exists_starts_with(TokenRef.MULTI_SYMBOLS, current_token + current_line[i + 1], False):
                    next_token = Token(TokenRef.MULTI_SYMBOLS[current_token], current_token)
                    current_token = ""
        elif exists_starts_with(TokenRef.KEYWORDS, current_token, False):
            if current_token in TokenRef.KEYWORDS:
                next_token = Token(TokenType.KEYWORD, current_token)
        elif current_token.isalpha():
            if i == len(current_line) - 1:
                next_token = Token(TokenType.IDENTIFIER, current_token)
            elif not current_line[i + 1].isalpha():
                next_token = Token(TokenType.IDENTIFIER, current_token)
        else:
            print("UNKNOWN: " + current_token + " at " + str(row))
            exit(1)

        if next_token is not None:
            return (current_line[i + 1:], next_token)

def tokenise_line(line: str) -> List[Token]:
    global row
    row += 1
    line_tokens: List[Token] = []
    while not line.strip() == "":
        next_tok: Token
        line, next_tok = get_next_token(line)
        line_tokens.append(next_tok)
    return line_tokens
        
def tokenise_file(file_path: str) -> List[Token]:
    # TODO
    file_contents: List[str] = []
    tokens: List[Token] = []
    try:
        with open(file_path, 'r') as f:
            file_contents = f.readlines()
    except FileNotFoundError:
        kahvia.error(f"The file `{file_path}` could not be found", False)
    except PermissionError:
        kahvia.error(f"Your user does not have permission to read the file `{file_path}`", False)
    except ValueError:
        kahvia.error(f"There was an error reading the encoding of the file `{file_path}`", False)
    except:
        kahvia.error(f"Unknown error reading the file `{file_path}`", False)

    for line in file_contents:
        if line == "":
            continue
        tokens.extend(tokenise_line(line))
        
    return tokens
