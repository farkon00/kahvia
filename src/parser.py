from src.tokentype import TokenType
import kahvia

def token_type_assert(token, type):
    if token.typ != type:
        kahvia.error(f"Syntax Error: Expected {type} but got {token.typ}", False)

def check_next_token(token, type):
    token_type_assert(token, type)
    return token.val

class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value  

class Parser:
    def __init__(self, tokens):
        self.vars = []
        self.tokens = tokens
    
    def parse_tokens(self):
        current_token_index = 0
        while current_token_index < len(self.tokens):
            token = self.tokens[current_token_index]
            if token.typ == TokenType.KEYWORD:
                if token.val == "var":
                    # Definition of a variable
                    current_token_index += 1
                    variable_type = check_next_token(self.tokens[current_token_index], TokenType.KEYWORD)
                    current_token_index += 1
                    var_name = check_next_token(self.tokens[current_token_index], TokenType.IDENTIFIER)
                    current_token_index += 1
                    check_next_token(self.tokens[current_token_index], TokenType.SET)
                    current_token_index += 1
                    if variable_type == "int":
                        value = check_next_token(self.tokens[current_token_index], TokenType.INTEGER)
                    else:
                        kahvia.error(f"Invalid variable type: {variable_type}", False)
                    self.vars.append(Variable(var_name, value))
            current_token_index += 1
        print("Parsing finished successfully!")
        for var in self.vars:
            print(f"Variable: {var.name} = {var.value}")