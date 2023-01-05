#!/usr/bin/python3
length= len(sentence)
first= sentence[0]
def multiple_returns(sentence):
    if len(sentence)==0:
        first= ''
    else:
        print("Length: {:d} - First character: {}".format(length, first))
