# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"

import math
def get_middle(s):
    string = list(s)
    resultado = []
    #validación para las palabres pares
    if len(string) %2 ==0:
        posicion = int(len(string)/2)
        resultado.append(string[(posicion-1)])
        resultado.append(string[posicion])
        return "".join(resultado)
    #para los que son solo una letra
    elif len(string) == 1:
        return s
    #para los que son impares
    else:
        posicion =  math.floor((len(string)/2))
        return string[posicion]