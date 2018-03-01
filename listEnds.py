# This program prints first and last elements of a list
# The list is randomly produced
#
# Copyright 2018, Eric Dawson, All rights reserved.

# Import modules
import random

# Functions and Classes
def randList(listRange, listLength):
    """ (int, int) -> list
    Returns list of random numbers
    in given range and of given length
    """
    rand_list = []
    for i in range(listLength):
        rand_list.append(random.randint(0,listRange))
    
    return rand_list

def listEnds(L):
    """ (list) -> list
    Returns first and last elements of a given list
    >>> listEnds([])
    []
    >>> listEnds([1])
    [1, 1]
    >>> listEnds([1, 2, 3])
    [1, 3]
    """
    # Check for empty list
    if L == []:
        return L
    newList = []
    newList.append(L[0])
    newList.append(L[-1])

    return newList

def main():
    # Calls for a list of 20 random numbers
    # in the range 1-100
    L = randList(100, 20)
    print("The original list :")
    print(L)
    print("")
    print("The list ends are :")
    print(listEnds(L))
    print("")

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
