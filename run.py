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
    """
    Contains the main function that has the loop that controls the game.
    """
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
    """
    Creates the ships randomly on the computers board.
    """
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(4):
            self.numbers, self.letters = randint(0, 7), randint(0, 7)
            while self.board[self.numbers][self.letters] == 'X':
                self.numbers, self.letters = randint(0, 7), randint(0, 7)
            self.board[self.numbers][self.letters] = 'X'
        return self.board

    @staticmethod
    def get_user_input():
        """
        Gets the users choice to try and hit the computers ships.
        """
        try:
            numbers = input('Please enter a number from the board: ')
            while numbers not in ('1', '2', '3', '4', '5', '6', '7', '8'):
                print(
                    'That is not a valid choice'
                    ' please select a number between 1-8.'
                )
                numbers = input('Please enter a number from the board: ')

            letters = input('Please enter a letter from the board: ').upper()
            while letters not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
                print(
                    'That is not a valid choice'
                    ' please select a letter from A-H: '
                )
                letters = input(
                    'Please enter a letter from the board: '
                ).upper()
            return int(numbers) - 1, LETTERS_TO_NUMS[letters]
        except ValueError and KeyError:
            print('That is not a valid input')
            return Battleship.get_user_input()

    def count_hit_ships(self):
        """
        Counts to see if there are any ships hit.
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == 'X':
                    hit_ships += 1
        return hit_ships


def RunGame():
    """
    Runs the game and print interactive comments to user.
    """
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
            print('You already made that guess.')
            user_x_row, user_y_column = Battleship.get_user_input()
        if computer_board.board[user_x_row][user_y_column] == 'X':
            print('Yay for you! You sunk one of my battleships')
            user_guess_board.board[user_x_row][user_y_column] = 'X'
        else:
            print('Sorry, you missed!')
            user_guess_board.board[user_x_row][user_y_column] = '-'
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print('Congratulations, you just hit all of my battleships!')
            break
        else:
            turns -= 1
            print(f'You have {turns} turns remaining.')
            if turns == 0:
                print("I'm sorry, you ran out of turns.")
                break


if __name__ == '__main__':
    RunGame()
    """
    Plays the Game.
    """