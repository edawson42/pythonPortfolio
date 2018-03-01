# List all divisors of the given number
#
# Copyright 2018, Eric Dawson, All rights reserved.

def getNumber(prompt):
    """ (str) -> (object)

    Returns output from user.
    """
    output = input(prompt)
    while output.isdigit() == False:
        print('Please enter number values only.')
        output = input(prompt)
    return output

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

if __name__ == '__main__':
    number = int(getNumber("Enter a number: "))
    print(listDivisors(number))
