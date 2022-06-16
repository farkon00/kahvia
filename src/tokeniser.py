import kahvia
from src.tokentype import Token, TokenType
from typing import List

# Tokeniser

def tokenise_file(file_path: str) -> List[TokenType]:
    # TODO
    file_contents: List[str] = []
    tokens: List[TokenType] = []
    try:
        with open(file_path, 'r') as f:
            file_contents = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        kahvia.error(f"The file `{file_path}` could not be found", False)
    except PermissionError:
        kahvia.error(f"Your user does not have permission to read the file `{file_path}`", False)
    except ValueError:
        kahvia.error(f"There was an error reading the encoding of the file `{file_path}`", False)
    except:
        kahvia.error(f"Unknown error reading the file `{file_path}`", False)

    return tokens
