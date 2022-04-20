# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.


def positive_sum(arr):
    #lista para guardar los números positivos
    resultado = [0]
    #agre
    for i in arr:
        if i > 0:
            resultado.append(i)
    #resultado que suma todos los positivos
    return sum(resultado)
