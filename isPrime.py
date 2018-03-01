# This program determines if given number is prime
#
# Copyright 2018, Eric Dawson, All rights reserved.

# Functions and Classes

def listDivisors(number):
    """ (int) - list
    Returns list of all divisors of given number
    >>> listDivisors(0)
    []
    >>> listDivisors(1)
    [1]
    >>> listDivisors(9)
    [1, 3, 9]
    """
    divisorList = []

    for i in range(1, number + 1):
        if number % i == 0:
            divisorList.append(i)
    return divisorList

def isPrime(num):
    """ (int) -> bool
    Returns True if number is prime
    Otherwise returns False
    >>> isPrime(5)
    True
    >>> isPrime(8)
    False
    """
    divisors = listDivisors(num)
    if len(divisors) == 2:
        return True
    else:
        return False

def getNumber(prompt):
    """ (str) -> int

    Returns output from user.
    """
    output = input(prompt)
    while output.isdigit() == False:
        print('Please enter number values only.')
        output = input(prompt)
    return int(output)

def main():
    print("")
    print("Prime number check.")
    number = getNumber("Please enter a number :")
    print("")
    if isPrime(number):
        print("The number %i is a prime number." % number)
    else:
        print("The number %i is NOT a prime number." % number)

if __name__ == '__main__':
    import time
    import doctest
    doctest.testmod()

    start_time = time.clock()
    # Runs main program
    main()
    # Computes runtime of program and prints
    print("")
    print("")
    print("--- %s seconds ---" % (time.clock() - start_time))
