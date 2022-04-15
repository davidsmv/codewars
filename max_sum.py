# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.


def max_sequence(arr):
    #lista que va almacenar todos los resultados de las operaciones
    results = []
    #cuenta los negativos
    contador = 0
    #variable para poder hacer las sumas
    suma = 0
    for x in arr:
        #para mirar si todos son negativos, si contador y el largo de la lista arr son iguales quiere decir que todos los datos son negativos
        if x<0:
            contador = contador +1
    if contador == len(arr):
        return 0
    else:
        #for que recorre y hace todas las sumas, hay dos for para poder recorrer y hacer todas las sumas
        for i in range(0,(len(arr))-1):
            suma = arr[i]
            for x in range((i+1),(len(arr))):
                suma  = suma+arr[x]
                #esto es para ir guardando los resultados, al final se escogera el valor más alto
                results.append(suma)
        return max(results)