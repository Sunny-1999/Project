# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




"""
Error to be corrected
is replacing input over other input instead of asking again
cannot take value except 1 to 9 
exceptioin handling for invalid input

"""
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
def player_input():
    marker=''
    while not(marker=='X' or marker=='O'):
        marker=(input('Player 1 select "X" or "O" : ' )).capitalize()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')
        
import random

def choose_first():
    if random.randint(0,1):
        return 'Player 1'
    else:
        return 'Player 2'
    
def place_marker(board,marker,position):
    board[position]=marker
    
def space_check(board,position):
    #Have to put error and exception handling in this method to make the game fully operational!
    if position in [0,1,2,3,4,5,6,7,8,9]:
        return board[position] == ' '
    else:
        return False
    
def player_choice(board,player_name):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] and space_check(board,position):
        position=int(input(player_name+' choose a number between 1-9 : '))
    return position

def full_check(board):
    for i in range(1,9):
        if space_check(board,i):
            return False
    return True

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))
    
def replay():
       return input('Do you want to play again? Enter Yes or No : ').lower().startswith('y')
   
    
    
print("lets play tic tac toe")

while True:
    the_board=[' ']*10
    player_1,player_2=player_input()
    turn=choose_first()
    print(turn+' will go first')
    go_on = True
    while go_on:
        if turn=="Player 1":
            display_board(the_board)
            position=player_choice(the_board,turn)
            place_marker(the_board,player_1,position)
            turn="Player 2"
            if win_check(the_board,player_1):
                display_board(the_board)
                print('player1 has win the game')
                go_on=False
            if full_check(the_board):
                display_board(the_board)
                print("the match is a draw")
                go_on=False
        else:
            display_board(the_board)
            position=player_choice(the_board,turn)
            place_marker(the_board,player_2,position)
            turn="Player 1"
            if win_check(the_board,player_2):
                display_board(the_board)
                print("player 2 has win the match")
                go_on=False
            if full_check(the_board):
                display_board(the_board)
                print('the match is a draw')
                go_on=False
    
    if not replay():
        break
                
