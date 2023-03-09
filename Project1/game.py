# import tkinter.messagebox

class Board:
    """
    A class to represent the game board for tic tac toe.

    ...

    Attributes
    ----------
    row1 : list of chars
        first row of game board
    row2 : list of chars
        second row of game board
    row3 : list of chars
        third row of game board

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, row1, row2, row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        pass

    def __str__(self):
        '''
        Print the current game board
        '''
        return f"{self.row1[0]} | {self.row1[1]} | {self.row1[2]}\n" +\
            f"{self.row2[0]} | {self.row2[1]} | {self.row2[2]}\n" +\
            f"{self.row3[0]} | {self.row3[1]} | {self.row3[2]}\n"
        # return f"{self.row1}\n{self.row2}\n{self.row3}"

    def end_state(self):
        '''
        Check if the current game has a winner and declear the winner

            Parameters: 
                None

            Return:
                (char): 'O' if 'O' wins
                        'X' if 'X' wins
                        'n' if there is no winner
        '''
        
        pass

# INIT_STATE = False


def init_board():
    '''
    Create an empty board
    '''
    # if INIT_STATE: pass
    row = ['*', '*', '*']
    row2 = ['O', 'O', 'X']
    game_board = Board(row, row, row)
    # INIT_STATE = True
    return game_board


def detect_input():
    '''
    Recieve user inputs and return the valid pair
    '''
    validation = True
    while validation:
        row = input("Please first enter the row number(1-3)")
        column = input("Please then enter the column number(1-3)")
        if not validate_input(int(row), int(column)):
            # tkinter.messagebox.showwarning(title="Error", message="Invalid input(s)")
            input("Invalid input(s), press Enter to redo")
        else:
            validation = False
    return int(row), int(column)


def validate_input(row, column):
    '''
    Check if the inputs are valid
    
        Parameters:
            row(int): Row number
            column(int): Column number
        
        Return:
            (boolean): Whether the inputs are valid or not
        '''
    if type(row) != int or type(column) != int:
        return False
    return row > 0 and row < 4 and column > 0 and column < 4




# game_board = Board([1, 2, 3], [" ", " ", " "], [" ", " ", " "])
# print(game_board)
# a, b = game_board.detect_input()
# game_board.validate_input(a, b)
gb = init_board()
print(gb)