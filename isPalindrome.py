# Get string from user and check if it is a palindrome
# 

# Copyright 2018, Eric Dawson, All rights reserved.

def getInput(prompt):
    """ (str) -> (object)

    Returns output from user.
    """
    output = input(prompt)
    while output.isalnum() == False:
        output = input(prompt)

    return output

def isPalindrome(inputString):
    """ (str) -> bool

    Returns True if string is a palindrome, otherwise returns False
    """
    reverseString = ""
    for ch in inputString:
        reverseString = ch + reverseString
    if reverseString == inputString:
        return True
    else:
        return False

if __name__ == '__main__':
    import time
    import doctest
    doctest.testmod()

    string = getInput("Enter a string: ")
    def main():
        if isPalindrome(string):
            print("{} is a palindrome.".format(string))
        else:
            print("{} is not a palindrome.".format(string))

    start_time = time.clock()
    main()
    print("")
    print("")
    print("--- %s seconds ---" % (time.clock() - start_time))
