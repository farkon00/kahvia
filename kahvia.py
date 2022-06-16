#!/usr/bin/env python3

import sys
import src.tokeniser as tk

def version():
    print("[VERSION INFORMATION]")
    print("    kahvia v0.0.1-alpha")

def usage():
    print("[USAGE]")
    print("    ./kahvia.py <flags> [input file]")
    print("[FLAGS]")
    print("    -v, --version    Print the version information.")
    print("    -h, --help       Print this message to stdout.")

def error(err_msg, print_usage=True):
    print(f"kahvia: [ERROR] {err_msg}.")
    if print_usage:
        usage()
    exit(1)

if __name__ == "__main__":
    sys.argv = sys.argv[1:]
    inp_file = ""
    flags = [] # This array will be appended to for each flag that doesn't halt execution (currently -h and -v)
    for (i, argument) in enumerate(sys.argv):
        if argument[0] == '-':
            # Flags
            if argument in ('-v', '--version'):
                version()
                exit(0)
            elif argument in ('-h', '--help'):
                usage()
                exit(0)
            else:
                error("Unknown flag: " + argument)
        else:
            # File
            if inp_file == "":
                inp_file = argument
            else:
                error("Too many files provided. Only one input file may be supplied", False)

    # We have the input file now :D
    print(tk.tokenise_file(inp_file))
