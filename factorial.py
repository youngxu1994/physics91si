#This is another file for fun.
#Recursively calculate the factorial of a given integer.

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
