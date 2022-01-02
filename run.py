from random import randint

HIDDEN_BOARD = [[' ']] * 6 for x in range(6)]
GUESS_BOARD = [[' ']] * 6 for x in range(6)]

letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}

def print_board(board):
    print('  A B C D E F')
    print('  -----------')
    row_number = 1
    for row in board:
        print('%d|%s|' % (row_number, '|'.join(row)))
        row_number += 1

def create_ships(board):
    for ship in range(4):
        ship_row, ship_column = randint(0,5), randint(0,5)
        while board[ship_row][ship_random] == 'X':
            ship_row, ship_column = randint(0,5), randint(0,5)
            


def get_ship_location():
    pass

def count_hit_ships():
    pass


