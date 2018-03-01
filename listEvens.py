#make new list of even numbers only from given list
#
# Copyright 2018, Eric Dawson, All rights reserved.

def listEvens(list):
    """ (list) -> list
    Returns list of even numbers from given list
    """
    evenList = [num for num in list if num % 2 == 0]
    return evenList

