# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)


def is_isogram(string):
    #contador que iniciara con el número negativo de lo largo del string
    contador = len(string)*-1
    for i in string.lower():
        for x in string.lower():
            if i == x:
                contador +=1
    if contador >0:
        return False
                   
    else:
        return True