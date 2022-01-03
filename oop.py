from random import randint

LETTERS_TO_NUMS = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}


class GameBoard:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        print('  A B C D E F G H')
        print('  ---------------')
        row_number = 1
        for row in self.board:
            print('%d|%s|' % (row_number, '|'.join(row)))
            row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(4):
            self.x_row, self.y_column = randint(0, 7), randint(0, 7)
            while self.board[self.x_row][self.y_column] == 'X':
                self.x_row, self.y_column = randint(0, 7), randint(0, 7)
            self.board[self.x_row][self.y_column] = 'X'
        return self.board

    @staticmethod
    def get_user_input():
        try:
            x_row = input('Enter the row of the ship: ')
            while x_row not in ('1', '2', '3', '4', '5', '6', '7', '8'):
                print('Not a valid choice, please select a valid row')
                x_row = input('Enter the row of the ship: ')

            y_column = input('Enter the letter of the ship: ').upper()
            while y_column not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
                print('Not a valid choice, please select a valid column: ')
                y_column = input(
                    'Enter the column letter of the ship: '
                ).upper()
            return int(x_row) - 1, LETTERS_TO_NUMS[y_column]
        except ValueError and KeyError:
            print('Not a valid input')
            return Battleship.get_user_input()

    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == 'X':
                    hit_ships += 1
        return hit_ships


def RunGame():
    computer_board = GameBoard([[' '] * 8 for i in range(8)])
    user_guess_board = GameBoard([[' '] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)
    turns = 10
    while turns > 0:
        GameBoard.print_board(user_guess_board)
        user_x_row, user_y_column = Battleship.get_user_input()
        while (
            user_guess_board.board[user_x_row][user_y_column] == '-' or
            user_guess_board.board[user_x_row][user_y_column] == 'X'
        ):
            print('You guessed that one already')
            user_x_row, user_y_column = Battleship.get_user_input()
        if computer_board.board[user_x_row][user_y_column] == 'X':
            print('You sunk one of my battleships')
            user_guess_board.board[user_x_row][user_y_column] = 'X'
        else:
            print('You missed!')
            user_guess_board.board[user_x_row][user_y_column] = '-'
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print('You hit all 5 battleships!')
            break
        else:
            turns -= 1
            print(f'You have {turns} turns remaining')
            if turns == 0:
                print("I'm sorry, you ran out of turns")
                GameBoard.print_board(user_guess_board)
                break


if __name__ == '__main__':
    RunGame()
