# Guessing game
# User guesses random generated number or enters exit to quit
# Counts number of correct guesses
# 
# Copyright 2018, Eric Dawson, All rights reserved.
import random

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


def printCorrect():
    print("")
    print("******************************")
    print("**        CORRECT!!         **")
    print("******************************")
    print("")

def printIncorrect():
    print("")
    print("******************************")
    print("**         WRONG!!          **")
    print("******************************")
    print("")
    
def playGame(guess, answer):
    correct_guesses = 0
    while guess != -1:
        if guess == answer:
            correct_guesses +=1
            printCorrect()
            print("%i is CORRECT!!!" % (guess))
            print("")
            print("That's %s correct so far!" % (correct_guesses))
            print("")
            print("Let's play again or type exit to quit.")
            print("")
            answer = random.randrange(1, 9)
            guess = getNumber(prompt)
        else:
            printIncorrect()
            print("%i is an incorrect guess. Try again." % (guess)) 
            print("")
            guess = getNumber(prompt)

def main(): 
    prompt = 'Please enter a number (1-9 only): '
    answer = random.randrange(1, 9)
    guess = getNumber(prompt)
    if guess != -1:
        playGame(guess, answer)

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