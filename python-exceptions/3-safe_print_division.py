#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except:
        pass
    finally:
        return "{:d}.format(c)"
