#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size != 0:
        frst = sentence[0]
        return size, frst
    else:
         return size, None
