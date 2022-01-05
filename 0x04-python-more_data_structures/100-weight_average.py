#!/usr/bin/python3
def weight_average(my_list=[]):
    numerador = sum(list(map(lambda tpl: tpl[0] * tpl[1], my_list)))
    denominador = sum(list(map(lambda tpl: tpl[1], my_list)))
    average = numerador / denominador
    return (average)
