#!/usr/bin/env python3
import sys

def valid_choices(board):
    '''valid_choices(list) -> list(tuples)

    returns a list of tuples of valid choices

    The below code is equivalent to:

    return [(row_i, col_i) for row_i,row in enumerate(board)
            for col_i,col in enumerate(row) if col == ' ']
    '''
    coordinates = []
    for row_i, row in enumerate(board):
        for col_i, col in enumerate(row):
            if col == ' ':
                coordinates.append((row_i, col_i))
    return coordinates


def validate_move(row, col, character, board):
    '''
    validate_move(char, char, char, list) -> bool

    given a row and a column, validate this move and update the board accordingly.
    '''
    try:
        # convert to index values
        p_row = int(row)
        p_col = int(col)
    except ValueError:
        return False

    # ensure index values are within the correct range
    if 0 > p_row < 2:
        return False
    if 0 > p_col < 2:
        return False

    # check to see that this is a valid move and update board if so
    if (p_row, p_col) in valid_choices(board):
        board[p_row][p_col] = character
        return True

    return False

def check_winner(board):
    '''
    check_winner(list) -> char or None

    check to see if there is a winner
    '''
    chars = ['X','O']
    
    # check rows
    for row in board:
        for char in chars:
            if all((col == char for col in row)):
                return char

    # check columns
    for c in range(3):
        for char in chars:
            if all((row[c] == char for row in board)):
                return char

    # check diagonals
    for char in chars:
        if all((board[i][i] == char for i in range(3))):
            return char
        if all((board[2-i][i] == char for i in range(3))):
            return char

    return None

def display_board(board):
    '''
    display_board(list) -> None

    print out the board using unicode characters
    '''
    print()
    print("\u2503".join(board[0]))
    print("\u2501\u252B\u2501\u2523\u2501")
    print("\u2503".join(board[1]))
    print("\u2501\u252B\u2501\u2523\u2501")
    print("\u2503".join(board[2]))
    print()

def main():
    '''
    main(None) -> int

    conducts the tic tac toe game logic
    '''
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    players = ((1, 'X'), (2, 'O'))

    keep_playing = True
    while keep_playing:
        for player in players:
            display_board(board)
            move = False
            
            # continue to prompt user until valid choice has been made
            while move is False:
                row = input(f"Player {player[0]} choose a row: ")
                col = input(f"Player {player[0]} choose a col: ")
                move = validate_move(row, col, player[1], board)
                
                if move is False:
                    print("\nInvalid Move\n")
            
            # check for a winner
            if check_winner(board) is not None:
                display_board(board)
                print(f"The winner is Player {player[0]}!!!")
                keep_playing = False
                break

            # check to see if board is full
            if len(valid_choices(board)) == 0:
                display_board(board)
                print("The game is a tie!!!")
                keep_playing = False
                break

    return 0


if __name__ == "__main__":
    sys.exit(main())
