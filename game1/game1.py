'''
1. Replace this block comment with a useful description of what this file and what your game is

Make the game start by running this file.

2. Python Objectives:
    a. Implement basic language features of Python (variables, ifs, loops, functions)
    b. Document your code with proper conventions
    c. Experiment with a debugger (a tutorial for the VSCode debugger is in Python workshop setup guide)

3. Game Objectives:
    a. Code a simple player vs computer game of your choice
    b. Winner of the game is decided on a function between the current state of the game and both player inputs
    c. A final winner may be decided after multiple rounds of input
    d. Example: tictactoe winner is decided based on current state of game and the player's input
    e. Tictactoe game board can be stored in a list, and the player input could be verified by making sure input is an open space
    
Author:
'''

def foo():
    ...

def main():
    '''You don't have to use this skeleton code'''

    #TODO: implement
    #game_state = new_game()

    while True:
        #TODO: prompt user to make a selection or call a function to retrieve it
        #needs validation
        user_choice = None 

        #TODO: select computer's choice or call a function to retrieve it
        computer_choice = None

        #TODO: decide and dispaly the results
        game_result = foo(game_state, user_choice, computer_choice)

        #TODO: implement quit or start new game condition
        if False:
            break

if __name__ == "__main__":
    main()