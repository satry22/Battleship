from random import randint

COMPUTER_BOARD = [[' '] * 6 for x in range(6)]
"""
Computers board
"""
GUESS_BOARD = [[' '] * 6 for x in range(6)]
"""
Players guessing board
"""

letters_to_nums = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}

def print_board(board):
    """
    Creates board
    """
    print('  A B C D E F')
    print('  -----------')
    row_number = 1
    for row in board:
        print('%d|%s|' % (row_number, '|'.join(row)))
        row_number += 1

def create_ships(board):
    """
    Creates Ship locations
    """
    for ship in range(4):
        ship_row, ship_column = randint(0,5), randint(0,5)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,5), randint(0,5)
        board[ship_row][ship_column] = 'X'
            
def get_ship_location():
    """
    Asks for Player to enter guess
    """
    row = input('Please enter a ship row 1-6: ')
    while row not in '123456':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-6: ')
    column = input('Please enter a ship column A-F: ').upper()
    while column not in 'ABCDEF':
        print('Please eneter a valid colum')
        column = input('Please eneter a ship column A-F: ').upper()
    return int(row) - 1, letters_to_nums[column]

def count_hit_ships(board):
    """
    Counts hit ships. Four ships wins.
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(COMPUTER_BOARD)
"""
Uses all of the above functions to play the game.
"""
turns = 8
while turns > 0:
    print('Welcome to Battleship!')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print('Oops! You already made that guess')
    elif COMPUTER_BOARD[row][column] == 'X':
        print('Congratulations, you just hit one of the Computers battleship!')
        turns -= 1
    else:
        print('Sorry, you missed this time')
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 4:
        print('Congratulations, you won the game!')
        break
    print('You have ' + str(turns) + ' turns left.')
    if turns == 0:
        print('Sorry, the game is over.')
        break