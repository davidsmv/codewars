# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!


def get_sum(a,b):
    data = [a, b]
    #sort the list
    data1 = sorted(data)
    result = 0
    for i in range(data1[0], data1[1]+1):
        if a!=b:
            result = result + (i)
        else:
            return a
    return result