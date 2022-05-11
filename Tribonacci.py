# Well met with Fibonacci bigger brother, AKA Tribonacci.

# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
# Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)



def tribonacci(signature, n):
    #para poder encontrar las posiciones en la lista
    a=0
    b=1
    c=2
    #lista para casos especiales (n = 0 o 1 o 2)
    lista = []
    #while para ir agregando los datos para n >3
    while len(signature) < n:
        signature.append(signature[a] + signature[b]+signature[c])
        a+=1
        b+=1
        c+=1
    #if para casos especiales  (n = 0 o 1 o 2)   
    if n == 1:
        lista.append(signature[0])
        return lista
    elif n == 0:
        return lista
    if n == 2:
        lista.append(signature[0])
        lista.append(signature[1])
        return lista
    #respuesta para casos no especiales
    else:
        return signature