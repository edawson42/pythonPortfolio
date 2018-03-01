# Create two random lists and print them sorted. 
# Then print list of common elements.
# 
# Copyright 2018, Eric Dawson, All rights reserved.
import random

def commonElements(L1, L2):
    """ (list, list) -> list

    Return list of elements common to two lists.

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> commonElements(a, b)
    []
    >>> a = [1, 2, 3]
    >>> b = [1, 4, 6]
    >>> commonElements(a, b)
    [1]
    >>> a = [1, 2, 3, 10]
    >>> b = [1, 2, 4, 6, 7, 10]
    >>> commonElements(a, b)
    [1, 2, 10]
    """
    new_list = []
    [new_list.append(a) for a in L1 for b in L2 if a == b and a not in new_list]

    return new_list

#create empty lists to fill with random numbers
rand_list1 = []
rand_list2 = []

#create two lists of random numbers using a random length
for i in range(random.randint(0, 20)):
    rand_list1.append(random.randint(0,50))
    
for i in range(random.randint(0, 50)):
    rand_list2.append(random.randint(0,500))

#sort the two lists
rand_list1.sort()
rand_list2.sort()

print('The first list: {}'.format(rand_list1))
print('The second list: {}'.format(rand_list2))

print('The common elements in both lists: ', commonElements(rand_list1, rand_list2))
      
if __name__ == '__main__':
    import doctest
    doctest.testmod()
