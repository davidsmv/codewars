# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

import string

def is_pangram(s):
    contador=0
    #for para sacar los datos únicos y en minuscula de la cadena string
    for i in set(list(s.lower())):
        # for para recorrer toda la cadena del abecedario en minuscula
        for x in string.ascii_lowercase:
            if i ==x:
                contador +=1
    # si el contador es igual al largo de la cadena del alfabeto quiere decir que es un pangram
    if contador == len(string.ascii_lowercase):
        return True
    else:
        return False