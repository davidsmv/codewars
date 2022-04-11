# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    #saca los caracteres únicos del string y los convierte en una lista
    unicos = list(dict.fromkeys(list(string)))
    resultado = {}
    #este if es para retornar el resultado si el string esta vacio
    if unicos == []:
        return resultado
    #en caso de que no etse vacio se ejecuta esto
    else:
        for i in unicos:
            #se crea la llave en el diccionario
            resultado[i]=0
            for x in string:
                if i ==x:
                    #se empieza a contar el número de caracteres
                    resultado[i]=resultado[i]+1
        return resultado
   