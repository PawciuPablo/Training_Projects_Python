#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

def display_board(board):
    print('\n'*100)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


# In[ ]:


def player_input():
    
    player1_marker = 'wrong'
    
    good_choices = ['X', 'O']
    
    while player1_marker not in good_choices:
        
        player1_marker = input('Hello Player 1! Please choose your marker (X or O): ')
        
        if player1_marker not in good_choices:
            print('Sorry, invalid input! Please choose X or O ')
    
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    
    return (player1_marker, player2_marker)


# In[ ]:


def place_marker(board, marker, position):
    board[position] = marker


# In[ ]:


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    else:
        return False


# In[ ]:


import random

def choose_first():
    who_is_first = random.randint(1, 2)
    
    if who_is_first == 1:
        return 'Player 1'
    else:
        return 'Player 2'


# In[ ]:


def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


# In[ ]:


def full_board_check(board):
    for i in range (1,10):
        if space_check(board, i):
            return False
    return True


# In[ ]:


def player_choice(board):
    
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    
        position = int(input('Please choose your next position (number 1-9): '))
    
    return position


# In[ ]:


def replay():
    
    answer = 'Wrong'
    
    while answer not in ['Y', 'N']:
        
        answer = input('Do you want to play again? (Y or N): ')
        
        if answer not in ['Y', 'N']:
            print('Please choose Y or N')
        else:
            if answer == 'Y':
                return True
            else:
                return False


# In[ ]:





# In[ ]:


print('Welcome to Tic Tac Toe!')

# While loop to keep running the game
while True:
    
    # Setting everything up
    Board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print('Lucky you ' + turn + '! You go first!')
    play_game = 'Wrong'
    
    while play_game not in ['Y', 'N']:
        
        play_game = input('Are you ready to play? Enter Y or N:' )
    
        if play_game not in ['Y', 'N']:
            print(' Please enter Y or N')
        else:
            if play_game == 'Y':
                game_on = True
            else:
                game_on = False

        while game_on:
            if turn == 'Player 1':
                display_board(Board)
                position = player_choice(Board)
                place_marker(Board, player1_marker, position)
                
                if win_check(Board, player1_marker):
                    display_board(Board)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(Board):
                        display_board(Board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'
            
            else:
                display_board(Board)
                position = player_choice(Board)
                place_marker(Board, player2_marker, position)

                if win_check(Board, player2_marker):
                    display_board(Board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(Board):
                        display_board(Board)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 1'

# Break out of the while loop
    if not replay():
        break


# In[ ]:




