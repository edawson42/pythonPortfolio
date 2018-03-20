# This program draws a game board
# size will be square using given number
#
# Copyright 2018, Eric Dawson, All rights reserved.

# Import modules

# Functions and Classes
def getNumber(prompt):
    """ (str) -> (object)

    Returns output from user.
    """
    output = input(prompt)
    if output.lower() == 'exit':
        return -1
    while output.isdigit() == False or int(output) > 9 or int(output) < 1:
        output = input(prompt)
    return int(output)

def drawBoard(size):
    for i in range(size):
        print(" ---" * size)
        print("|   " * size + "|")
    print(" ---" * size)

def main():
    size = getNumber("Enter size of board: ")
    drawBoard(size)


if __name__ == '__main__':
    import time
    import doctest
    doctest.testmod()

    start_time = time.clock()

    # Run main program
    main()

    # Computes runtime of program and prints
    print("")
    print("")
    print("--- %s seconds ---" % (time.clock() - start_time))
