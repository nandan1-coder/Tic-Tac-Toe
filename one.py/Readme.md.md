TIC TAC TOE GAME
=================

Name: Nandan Kumar Ray
ERP: RU-26-02777
E-mail: nandan.kumar@rungta.org

Project Title: Tic Tac Toe Game


1. PROJECT DESCRIPTION
----------------------

This project is a two-player console-based Tic Tac Toe game developed
using Python.

The game is played on a 3x3 board. Player X starts the game and Player O
plays next. Each player selects a position from 1 to 9. The program
checks whether a player has completed a row, column, or diagonal.

The program also handles invalid input, already occupied positions,
draw conditions, and allows the players to play again.


2. BOARD POSITION
-----------------

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9


3. FEATURES
-----------

- Two-player game
- 3x3 board
- Player X starts first
- Checks rows, columns and diagonals
- Checks for a draw
- Prevents invalid positions
- Prevents already occupied positions
- Handles non-numeric input
- Allows the game to be played again


4. LANGUAGE USED
----------------

Python 3


5. HOW TO RUN
-------------

Save the Python code as:

tic_tac_toe.py

Run the program using:

python tic_tac_toe.py


6. TEST CASES
--------------

TEST CASE 1: PLAYER X WINS
---------------------------

Input / Moves:

X = 1
O = 4
X = 2
O = 5
X = 3

Expected Output:

Player X wins!
Winning line: 1 2 3


TEST CASE 2: PLAYER O WINS
---------------------------

Input / Moves:

X = 1
O = 4
X = 2
O = 5
X = 9
O = 6

Expected Output:

Player O wins!
Winning line: 4 5 6


TEST CASE 3: INVALID POSITION ABOVE 9
--------------------------------------

Input:

10

Expected Output:

Invalid position. Enter a number from 1 to 9.


TEST CASE 4: INVALID POSITION BELOW 1
-------------------------------------

Input:

0

Expected Output:

Invalid position. Enter a number from 1 to 9.


TEST CASE 5: NON-NUMERIC INPUT
------------------------------

Input:

abc

Expected Output:

Invalid position. Enter a number from 1 to 9.


TEST CASE 6: POSITION ALREADY TAKEN
-----------------------------------

Input / Moves:

X = 1
O = 1

Expected Output:

Position already taken. Choose another position.


TEST CASE 7: DRAW
-----------------

Input / Moves:

X = 1
O = 2
X = 3
O = 5
X = 4
O = 6
X = 8
O = 7
X = 9

Expected Output:

Board is full after 9 moves. It's a draw! No moves left.


TEST CASE 8: PLAY AGAIN
-----------------------

After a game finishes, enter:

Play again? (y/n): y

Expected Result:

A new game starts with an empty board.


TEST CASE 9: EXIT GAME
----------------------

After a game finishes, enter:

Play again? (y/n): n

Expected Output:

Thank you for playing!


7. FUNCTIONS USED
-----------------

display_board(board)
Displays the current game board.

check_winner(board, player)
Checks all possible winning combinations.

play_game()
Controls the complete game, including player turns, input validation,
winner checking and draw checking.


8. CONCEPTS USED
----------------

- Lists
- Functions
- While loop
- For loop
- If-else statements
- Try-except
- Input validation
- String handling
- Game logic


9. CONCLUSION
-------------

The Tic Tac Toe Game is a simple Python project that demonstrates
basic programming concepts. It provides a complete two-player game
with winner detection, draw detection, input validation and replay
functionality.
