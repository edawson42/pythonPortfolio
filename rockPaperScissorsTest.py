# This program is a two player game
# Classic game of RockPaperScissors
# # Copyright 2018, Eric Dawson, All rights reserved.

# Functions and Classes

def getInput(prompt):
    """ (str) -> (object)
    Returns output from user.
    """
    output = input(prompt).lower()
    
    while output.isAlpha() == False \
          or not validInput(output):
        output = input("Must enter valid words. " + prompt).lower() 
    
    return output

def validInput(playerMove):
    """ (str) -> bool
    Returns True if input is valid move
    Otherwise returns False
    """
    valid = ['rock','scissors','paper']
    
    if playerMove in valid:
        return True
    else:
        return False

def gameWinner(player_1_move, player_2_move):
    """ (str, str) -> str
    Returns message stating winner of game
    """
    winner = "Player 1 WINS!"

    if player_1_move == player_2_move:
        winner = "Tie game."
    elif player_1_move == "rock":
        if player_2_move == "paper":
            winner = "Player 2 WINS!"
    elif player_1_move == "scissors":
        if player_2_move == "rock":
            winner = "Player 2 WINS!"
    elif player_1_move == "paper":
        if player_2_move == "scissors":
            winner = "Player 2 WINS!"
    
    return winner

def main():
    playAgain = "yes"
    while playAgain == 'yes':
        print("")
        print("To play, enter rock, paper, or scissors.")
        print("")
        player_1_move = getInput("Player 1. Enter your play: ")
        player_2_move = getInput("Player 2. Enter your play: ")
        print("")
        print(gameWinner(player_1_move, player_2_move))
        print("")
        playAgain = \
        input("Would you like to play Rock, Paper, Scissors? yes or no:").lower()
        print("")
        while playAgain not in ['yes','no']:
            playAgain = \
            input("Would you like to play Rock, Paper, Scissors? yes or no:").lower()
            print("")

if __name__ == '__main__':
    import time
    import doctest
    doctest.testmod()

    start_time = time.clock()
    main()
    print("--- %s seconds ---" % (time.clock() - start_time))
