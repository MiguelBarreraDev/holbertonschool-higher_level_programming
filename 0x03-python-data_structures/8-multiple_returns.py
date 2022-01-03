#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), None if sentence == "" else sentence[0])
