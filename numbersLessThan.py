# Functions that list numbers 
# less than given number from a list
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

def numbersLessThan(L, n):
    """ (List, int) -> List
    Returns list of numbers less than the given number
    from the given list
    """
    lessThan = [num for num in L if num < n]
    
    return lessThan

if __name__ == '__main__':
    L = [-1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print("Original list :")
    print(L)
    print("")
    number = int(getNumber("Enter number to get list of elements less than: "))
    print('List of elements less than', number, ': ')
    print(numbersLessThan(L, number))
