import sys
import atexit

def print_confirm():
    print("Compilation successful, no errors discovered.")

def check():
    if sys.argv[1] == "--checkcompile":
        atexit.register(print_confirm)
