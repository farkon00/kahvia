#!/usr/bin/env python3

import sys
import src.tokeniser as tk
import src.parser as parser

from typing import List

def version() -> None:
    print("[VERSION INFORMATION]")
    print("    kahvia v0.0.1-alpha")

    exit(0)

def usage(error: bool = False) -> None:
    print("[USAGE]")
    print("    ./kahvia.py <flags> [input file]")
    print("[FLAGS]")
    print("    -v, --version    Print the version information.")
    print("    -h, --help       Print this message to stdout.")

    exit(0 if not error else 1)

def error(err_msg: str, print_usage: bool=True) -> None:
    print(f"kahvia: [ERROR] {err_msg}.")
    print()
    if print_usage:
        usage(error=True)

    exit(1)

def main():
    args: List[str] = sys.argv[1:]
    inp_file: str = ""
    flags: List[str] = [] # This array will be appended to for each flag that doesn't halt execution (currently -h and -v)
    if len(args) == 0:
        error("No input file was provided")
    for argument in args:
        if argument[0] == '-':
            # Flags
            if argument in ('-v', '--version'):
                version()
            elif argument in ('-h', '--help'):
                usage()
            else:
                error(f"Unknown flag: {argument}")
        else:
            # File
            if not inp_file:
                inp_file = argument
            else:
                error("Too many files provided. Only one input file may be supplied", False)

    # We have the input file now :D
    tokens = tk.Tokeniser(inp_file).tokenise_file()
    for token in tokens:
        print(f"Token: {token.typ} {token.val}")
    ast = parser.Parser(tokens).parse_tokens()

if __name__ == "__main__":
    main()
