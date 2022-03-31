#Given an array of integers, find the one that appears an odd number of times. There will always be only one integer that appears an odd number of times.
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

import collections
def find_it(seq):
    #hace un diccionario contando cuantos hay de cada dato
    datos = collections.Counter(seq)
    for i in datos:
        if (datos[i] % 2) > 0:       
            return i

#sampletest

# import codewars_test as test
# from solution import find_it

# @test.describe("Sample tests")
# def sample_tests():
    
#     @test.it("find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) should return 5 (because it appears 3 times)")
#     def _():
#         test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
        
#     @test.it("find_it([1,1,2,-2,5,2,4,4,-1,-2,5]) should return -1 (because it appears 1 time)")
#     def _():
#         test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
        
#     @test.it("find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]) should return 5 (because it appears 3 times)")
#     def _():
#         test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
        
