![SCOA](https://github.com/stem-club-of-america/SCOA/blob/main/images/SCOA_Logo_Small.png)

# Tic Tac Toe
In this lab, we build the Tic Tac Toe game in python.  The game itself has easy logic and game-play so it can be completed in a decent amount of time. Advanced students may be able to complete this on their own.  Most students will need help.

![TicTacToe](https://github.com/stem-club-of-america/SCOA/blob/main/labs/tictactoe/images/tictactoe.png)

## Requirements
The sample lab code uses Unicode characters to represent the board.  In this day and age, every terminal should support Unicode.

## Topics that can be discussed as you're completing this lab
1. Keep main game logic simple.  This will hopefully keep the main logic easy to read and understand.  The mechanics of implementing that logic, should be captured in other functions.
2. The board can be represented as a list of lists where the first index value represents the row and the second index value represents the column: `board[row][col]`
3. The `enumerate` function returns a tuple of `(index, value)` which makes it excellent to loop across our board.
4. The `all` function evaluates all elements of an iterable to determine if they are all `True`.  It returns `False` as soon as it finds a `False` entry to efficiently fail fast by not evaluating further entries in the iterable.
5. **List Comprehensions** may look weird at first glance but are very powerful to transform one list into another list.
6. **Generator Expressions** may also look weird but lazily evaluate meaning that they return results as needed.  When used with functions like `all`, because it fails fast, you won't waste time building items that you'll never use.

## Utility Functions
* `valid_choices(board)` -> returns a list of tuples of valid choices
* `validate_move(row, col, character, board)` -> given a row and a column, validate this move and update the board accordingly
* `check_winner(board)` -> check to see if there is a winner
* `display_board(board)` -> print out the board using Unicode characters

