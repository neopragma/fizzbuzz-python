# -*- coding: utf-8 -*- 

def percolate(input: int):
    if input % 15 == 0: return 'FizzBuzz'
    if input % 5 == 0: return 'Buzz'
    if input % 3 == 0: return 'Fizz'
    return str(input) 

def process(values: range):
    result = ''
    for input in values:
        result += percolate(input) + "\n"
    return result