from random import randint

HIDDEN_BOARD = [[' '] * 6 for x in range(6)]
GUESS_BOARD = [[' '] * 6 for x in range(6)]

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
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,5), randint(0,5)
        board[ship_row][ship_column] = 'X'
            
def get_ship_location():
    row = input('Please enter a ship row 1-6')
    while row not in '123456':
        print('Please enter a valid row')
        row = input('Please enter a ship row 1-6')
    column = input('Please enter a ship column A-F').upper()
    while column not in 'ABCDEF':
        print('Please eneter a valid colum')
        column = input('Please eneter a ship column A-F').upper()
    return int(row) -1, letters_to_numbers(column)


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(HIDDEN_BOARD)
turns = 10
print_board(HIDDEN_BOARD)
print_board(GUESS_BOARD)

