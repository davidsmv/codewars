# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""


def order(sentence):
    #crea una lista donde guarda toda la sentence, la idea es que después de creada se empiece a modificar los datos de cada posoción según el orden
    resultado = sentence.split()
    #para comprobar si la sentencia etsa vacia
    if sentence == "":
        return ""
    else:
        for i in sentence.split():
            for n in i:
                try:
                    #ir guardando la posición/número
                    numero = int(n)
                    #guarda la palabra según la posición (número) en la lista ya creada (resultado)
                    resultado[numero-1]=i
                except: continue
        return " ".join(resultado)