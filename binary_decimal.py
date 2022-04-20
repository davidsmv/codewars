# <!-- Given an array of ones and zeroes, convert the equivalent binary value to an integer.

# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11 -->



def binary_array_to_number(arr):
    #variable que va a guardar el número binario en string, debe ser string para la función int al final
    bi = ''  
    for i in arr:
        #solo se tomará los números que están después del primer 0
        if len(bi) ==0 and i == 0:
            continue
        #se agregan los números a la variable
        else:
            bi = bi + str(i)
    #se valida que la variable no quede sola
    if bi == '':
        bi = '0'
        #se usa la función int para convertirlo a decimal
    return int((bi), 2)