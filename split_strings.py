# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']

def solution(s):
 pareja = ""
 resultado = []
 contador = 0
 igualador = 0
 for i in s:
    pareja = pareja + i  
    contador = contador + 1
    #este igualador es para mirar donde se acaba el for y poder agregar el "_"
    igualador = igualador +1
    # agrega el "_" si el total de datos es impar y cierra el ciclo
    if igualador %2 >0 and len(s) == igualador:
        resultado.append(pareja+"_")
    #este agrega la pareja de caracteres
    if contador == 2:
        resultado.append(pareja)
        contador = 0
        pareja = ""
 return resultado