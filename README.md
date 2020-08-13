# Ultimate Tic Tac Toe Zero

Ultimate Tic Tac Toe is a variation of the classic game Tic-Tac-Toe in which the game is played on a 9 by 9 board.

![UTTT.gif](https://github.com/antoniojkim/Ultimate-Tic-Tac-Toe-Zero/tree/master/Images/UTTT.gif)

The game logic was implemented in C++ for performance reasons and imported into python using ctypes to create a simple GUI using PyQT5.

## Game AI

### [Monte Carlo Tree Search (MCTS)](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)

For the baseline, original game AI, MCTS was used to great effect. In order to get superhuman performance, the algorithm requires 2.5 million iterations of MCTS run for every move which equates to approximately 5 seconds of thinking time.

It was implemented in C++ for performance and then imported into python using ctypes to be tested against the other AIs.
