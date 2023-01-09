#!/usr/bin/python3
def safe_print_integer_err(value,message):
    for i in value:
        try:
            print("{}".format(value))
            return True
        except (ValueError,IndexError):
            raise (message)
            return False
    return value
