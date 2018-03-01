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

number = int(getNumber("Enter a number: "))
divisor = int(getNumber("Enter a divisor to check: "))

def oddOrEven(number):
    """ (int) -> str
    Returns 'even' if num is even number
    Otherwise returns 'odd'
    >>> oddOrEven(4)
    'even'
    >>> oddOrEven(5)
    'odd'
    """
    result = 'even'
    if number % 2 != 0:
        result = 'odd'
    return result

print('\n')
print('The number %i is %s.' %(number, oddOrEven(number)))

if number % 4 == 0:
    print('The number %i is divisible by 4.' %(number))

if divisor != 0 and number % divisor == 0:
    print('The number %i is divisible by %i.' %(number, divisor))
else:
    print('The number %i is not divisible by %i.' %(number, divisor))

if __name__ == '__main__':
    import time
    import doctest
    doctest.testmod()