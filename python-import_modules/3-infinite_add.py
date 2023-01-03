#!/usr/bin/python3
if __name__ == "__main__:
    def sum_all(*args):
        try:
            return sum(int(i) for i in args)
        except:
            return False
print(sum_all())
