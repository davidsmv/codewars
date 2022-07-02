# You are given a string S.
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    
    
    s = input()

#any function that returns True if the iterable has at least one element iqual to True, otherwise will return False
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))