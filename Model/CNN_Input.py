from Game.Boards import P1, P2
from Game.Pure_MCTS.MCTS_Node import MCTS_Node
from numpy import array as np_array


def f1(i):
    """
    filter player 1
    :param i: integer value
    :return: either 0 or 1
    """
    return 1 if i == P1 else 0

def f2(i):
    """
    filter player 2
    :param i: integer value
    :return: either 0 or 1
    """
    return 1 if i == P2 else 0

def create_cnn_input(node: MCTS_Node):
    b = node.board
    b1 = [[f1(b[0][0]), f1(b[0][1]), f1(b[0][2]), f1(b[0][3]), f1(b[0][4]), f1(b[0][5]), f1(b[0][6]), f1(b[0][7]), f1(b[0][8])],
          [f1(b[1][0]), f1(b[1][1]), f1(b[1][2]), f1(b[1][3]), f1(b[1][4]), f1(b[1][5]), f1(b[1][6]), f1(b[1][7]), f1(b[1][8])],
          [f1(b[2][0]), f1(b[2][1]), f1(b[2][2]), f1(b[2][3]), f1(b[2][4]), f1(b[2][5]), f1(b[2][6]), f1(b[2][7]), f1(b[2][8])],
          [f1(b[3][0]), f1(b[3][1]), f1(b[3][2]), f1(b[3][3]), f1(b[3][4]), f1(b[3][5]), f1(b[3][6]), f1(b[3][7]), f1(b[3][8])],
          [f1(b[4][0]), f1(b[4][1]), f1(b[4][2]), f1(b[4][3]), f1(b[4][4]), f1(b[4][5]), f1(b[4][6]), f1(b[4][7]), f1(b[4][8])],
          [f1(b[5][0]), f1(b[5][1]), f1(b[5][2]), f1(b[5][3]), f1(b[5][4]), f1(b[5][5]), f1(b[5][6]), f1(b[5][7]), f1(b[5][8])],
          [f1(b[6][0]), f1(b[6][1]), f1(b[6][2]), f1(b[6][3]), f1(b[6][4]), f1(b[6][5]), f1(b[6][6]), f1(b[6][7]), f1(b[6][8])],
          [f1(b[7][0]), f1(b[7][1]), f1(b[7][2]), f1(b[7][3]), f1(b[7][4]), f1(b[7][5]), f1(b[7][6]), f1(b[7][7]), f1(b[7][8])],
          [f1(b[8][0]), f1(b[8][1]), f1(b[8][2]), f1(b[8][3]), f1(b[8][4]), f1(b[8][5]), f1(b[8][6]), f1(b[8][7]), f1(b[8][8])]]
    b2 = [[f2(b[0][0]), f2(b[0][1]), f2(b[0][2]), f2(b[0][3]), f2(b[0][4]), f2(b[0][5]), f2(b[0][6]), f2(b[0][7]), f2(b[0][8])],
         [f2(b[1][0]), f2(b[1][1]), f2(b[1][2]), f2(b[1][3]), f2(b[1][4]), f2(b[1][5]), f2(b[1][6]), f2(b[1][7]), f2(b[1][8])],
         [f2(b[2][0]), f2(b[2][1]), f2(b[2][2]), f2(b[2][3]), f2(b[2][4]), f2(b[2][5]), f2(b[2][6]), f2(b[2][7]), f2(b[2][8])],
         [f2(b[3][0]), f2(b[3][1]), f2(b[3][2]), f2(b[3][3]), f2(b[3][4]), f2(b[3][5]), f2(b[3][6]), f2(b[3][7]), f2(b[3][8])],
         [f2(b[4][0]), f2(b[4][1]), f2(b[4][2]), f2(b[4][3]), f2(b[4][4]), f2(b[4][5]), f2(b[4][6]), f2(b[4][7]), f2(b[4][8])],
         [f2(b[5][0]), f2(b[5][1]), f2(b[5][2]), f2(b[5][3]), f2(b[5][4]), f2(b[5][5]), f2(b[5][6]), f2(b[5][7]), f2(b[5][8])],
         [f2(b[6][0]), f2(b[6][1]), f2(b[6][2]), f2(b[6][3]), f2(b[6][4]), f2(b[6][5]), f2(b[6][6]), f2(b[6][7]), f2(b[6][8])],
         [f2(b[7][0]), f2(b[7][1]), f2(b[7][2]), f2(b[7][3]), f2(b[7][4]), f2(b[7][5]), f2(b[7][6]), f2(b[7][7]), f2(b[7][8])],
         [f2(b[8][0]), f2(b[8][1]), f2(b[8][2]), f2(b[8][3]), f2(b[8][4]), f2(b[8][5]), f2(b[8][6]), f2(b[8][7]), f2(b[8][8])]]
    return np_array([
        b1, b2,

        [[b1[8][0], b1[7][0], b1[6][0], b1[5][0], b1[4][0], b1[3][0], b1[2][0], b1[1][0], b1[0][0]],
         [b1[8][1], b1[7][1], b1[6][1], b1[5][1], b1[4][1], b1[3][1], b1[2][1], b1[1][1], b1[0][1]],
         [b1[8][2], b1[7][2], b1[6][2], b1[5][2], b1[4][2], b1[3][2], b1[2][2], b1[1][2], b1[0][2]],
         [b1[8][3], b1[7][3], b1[6][3], b1[5][3], b1[4][3], b1[3][3], b1[2][3], b1[1][3], b1[0][3]],
         [b1[8][4], b1[7][4], b1[6][4], b1[5][4], b1[4][4], b1[3][4], b1[2][4], b1[1][4], b1[0][4]],
         [b1[8][5], b1[7][5], b1[6][5], b1[5][5], b1[4][5], b1[3][5], b1[2][5], b1[1][5], b1[0][5]],
         [b1[8][6], b1[7][6], b1[6][6], b1[5][6], b1[4][6], b1[3][6], b1[2][6], b1[1][6], b1[0][6]],
         [b1[8][7], b1[7][7], b1[6][7], b1[5][7], b1[4][7], b1[3][7], b1[2][7], b1[1][7], b1[0][7]],
         [b1[8][8], b1[7][8], b1[6][8], b1[5][8], b1[4][8], b1[3][8], b1[2][8], b1[1][8], b1[0][8]]],

        [[b1[8][8], b1[8][7], b1[8][6], b1[8][5], b1[8][4], b1[8][3], b1[8][2], b1[8][1], b1[8][0]],
         [b1[7][8], b1[7][7], b1[7][6], b1[7][5], b1[7][4], b1[7][3], b1[7][2], b1[7][1], b1[7][0]],
         [b1[6][8], b1[6][7], b1[6][6], b1[6][5], b1[6][4], b1[6][3], b1[6][2], b1[6][1], b1[6][0]],
         [b1[5][8], b1[5][7], b1[5][6], b1[5][5], b1[5][4], b1[5][3], b1[5][2], b1[5][1], b1[5][0]],
         [b1[4][8], b1[4][7], b1[4][6], b1[4][5], b1[4][4], b1[4][3], b1[4][2], b1[4][1], b1[4][0]],
         [b1[3][8], b1[3][7], b1[3][6], b1[3][5], b1[3][4], b1[3][3], b1[3][2], b1[3][1], b1[3][0]],
         [b1[2][8], b1[2][7], b1[2][6], b1[2][5], b1[2][4], b1[2][3], b1[2][2], b1[2][1], b1[2][0]],
         [b1[1][8], b1[1][7], b1[1][6], b1[1][5], b1[1][4], b1[1][3], b1[1][2], b1[1][1], b1[1][0]],
         [b1[0][8], b1[0][7], b1[0][6], b1[0][5], b1[0][4], b1[0][3], b1[0][2], b1[0][1], b1[0][0]]],

        [[b1[0][8], b1[1][8], b1[2][8], b1[3][8], b1[4][8], b1[5][8], b1[6][8], b1[7][8], b1[8][8]],
         [b1[0][7], b1[1][7], b1[2][7], b1[3][7], b1[4][7], b1[5][7], b1[6][7], b1[7][7], b1[8][7]],
         [b1[0][6], b1[1][6], b1[2][6], b1[3][6], b1[4][6], b1[5][6], b1[6][6], b1[7][6], b1[8][6]],
         [b1[0][5], b1[1][5], b1[2][5], b1[3][5], b1[4][5], b1[5][5], b1[6][5], b1[7][5], b1[8][5]],
         [b1[0][4], b1[1][4], b1[2][4], b1[3][4], b1[4][4], b1[5][4], b1[6][4], b1[7][4], b1[8][4]],
         [b1[0][3], b1[1][3], b1[2][3], b1[3][3], b1[4][3], b1[5][3], b1[6][3], b1[7][3], b1[8][3]],
         [b1[0][2], b1[1][2], b1[2][2], b1[3][2], b1[4][2], b1[5][2], b1[6][2], b1[7][2], b1[8][2]],
         [b1[0][1], b1[1][1], b1[2][1], b1[3][1], b1[4][1], b1[5][1], b1[6][1], b1[7][1], b1[8][1]],
         [b1[0][0], b1[1][0], b1[2][0], b1[3][0], b1[4][0], b1[5][0], b1[6][0], b1[7][0], b1[8][0]]],

        [[b1[0][8], b1[0][7], b1[0][6], b1[0][5], b1[0][4], b1[0][3], b1[0][2], b1[0][1], b1[0][0]],
         [b1[1][8], b1[1][7], b1[1][6], b1[1][5], b1[1][4], b1[1][3], b1[1][2], b1[1][1], b1[1][0]],
         [b1[2][8], b1[2][7], b1[2][6], b1[2][5], b1[2][4], b1[2][3], b1[2][2], b1[2][1], b1[2][0]],
         [b1[3][8], b1[3][7], b1[3][6], b1[3][5], b1[3][4], b1[3][3], b1[3][2], b1[3][1], b1[3][0]],
         [b1[4][8], b1[4][7], b1[4][6], b1[4][5], b1[4][4], b1[4][3], b1[4][2], b1[4][1], b1[4][0]],
         [b1[5][8], b1[5][7], b1[5][6], b1[5][5], b1[5][4], b1[5][3], b1[5][2], b1[5][1], b1[5][0]],
         [b1[6][8], b1[6][7], b1[6][6], b1[6][5], b1[6][4], b1[6][3], b1[6][2], b1[6][1], b1[6][0]],
         [b1[7][8], b1[7][7], b1[7][6], b1[7][5], b1[7][4], b1[7][3], b1[7][2], b1[7][1], b1[7][0]],
         [b1[8][8], b1[8][7], b1[8][6], b1[8][5], b1[8][4], b1[8][3], b1[8][2], b1[8][1], b1[8][0]]],

        [[b1[8][8], b1[7][8], b1[6][8], b1[5][8], b1[4][8], b1[3][8], b1[2][8], b1[1][8], b1[0][8]],
         [b1[8][7], b1[7][7], b1[6][7], b1[5][7], b1[4][7], b1[3][7], b1[2][7], b1[1][7], b1[0][7]],
         [b1[8][6], b1[7][6], b1[6][6], b1[5][6], b1[4][6], b1[3][6], b1[2][6], b1[1][6], b1[0][6]],
         [b1[8][5], b1[7][5], b1[6][5], b1[5][5], b1[4][5], b1[3][5], b1[2][5], b1[1][5], b1[0][5]],
         [b1[8][4], b1[7][4], b1[6][4], b1[5][4], b1[4][4], b1[3][4], b1[2][4], b1[1][4], b1[0][4]],
         [b1[8][3], b1[7][3], b1[6][3], b1[5][3], b1[4][3], b1[3][3], b1[2][3], b1[1][3], b1[0][3]],
         [b1[8][2], b1[7][2], b1[6][2], b1[5][2], b1[4][2], b1[3][2], b1[2][2], b1[1][2], b1[0][2]],
         [b1[8][1], b1[7][1], b1[6][1], b1[5][1], b1[4][1], b1[3][1], b1[2][1], b1[1][1], b1[0][1]],
         [b1[8][0], b1[7][0], b1[6][0], b1[5][0], b1[4][0], b1[3][0], b1[2][0], b1[1][0], b1[0][0]]],

        [[b1[8][0], b1[8][1], b1[8][2], b1[8][3], b1[8][4], b1[8][5], b1[8][6], b1[8][7], b1[8][8]],
         [b1[7][0], b1[7][1], b1[7][2], b1[7][3], b1[7][4], b1[7][5], b1[7][6], b1[7][7], b1[7][8]],
         [b1[6][0], b1[6][1], b1[6][2], b1[6][3], b1[6][4], b1[6][5], b1[6][6], b1[6][7], b1[6][8]],
         [b1[5][0], b1[5][1], b1[5][2], b1[5][3], b1[5][4], b1[5][5], b1[5][6], b1[5][7], b1[5][8]],
         [b1[4][0], b1[4][1], b1[4][2], b1[4][3], b1[4][4], b1[4][5], b1[4][6], b1[4][7], b1[4][8]],
         [b1[3][0], b1[3][1], b1[3][2], b1[3][3], b1[3][4], b1[3][5], b1[3][6], b1[3][7], b1[3][8]],
         [b1[2][0], b1[2][1], b1[2][2], b1[2][3], b1[2][4], b1[2][5], b1[2][6], b1[2][7], b1[2][8]],
         [b1[1][0], b1[1][1], b1[1][2], b1[1][3], b1[1][4], b1[1][5], b1[1][6], b1[1][7], b1[1][8]],
         [b1[0][0], b1[0][1], b1[0][2], b1[0][3], b1[0][4], b1[0][5], b1[0][6], b1[0][7], b1[0][8]]],

        [[b1[0][0], b1[1][0], b1[2][0], b1[3][0], b1[4][0], b1[5][0], b1[6][0], b1[7][0], b1[8][0]],
         [b1[0][1], b1[1][1], b1[2][1], b1[3][1], b1[4][1], b1[5][1], b1[6][1], b1[7][1], b1[8][1]],
         [b1[0][2], b1[1][2], b1[2][2], b1[3][2], b1[4][2], b1[5][2], b1[6][2], b1[7][2], b1[8][2]],
         [b1[0][3], b1[1][3], b1[2][3], b1[3][3], b1[4][3], b1[5][3], b1[6][3], b1[7][3], b1[8][3]],
         [b1[0][4], b1[1][4], b1[2][4], b1[3][4], b1[4][4], b1[5][4], b1[6][4], b1[7][4], b1[8][4]],
         [b1[0][5], b1[1][5], b1[2][5], b1[3][5], b1[4][5], b1[5][5], b1[6][5], b1[7][5], b1[8][5]],
         [b1[0][6], b1[1][6], b1[2][6], b1[3][6], b1[4][6], b1[5][6], b1[6][6], b1[7][6], b1[8][6]],
         [b1[0][7], b1[1][7], b1[2][7], b1[3][7], b1[4][7], b1[5][7], b1[6][7], b1[7][7], b1[8][7]],
         [b1[0][8], b1[1][8], b1[2][8], b1[3][8], b1[4][8], b1[5][8], b1[6][8], b1[7][8], b1[8][8]]],

        [[b2[8][0], b2[7][0], b2[6][0], b2[5][0], b2[4][0], b2[3][0], b2[2][0], b2[1][0], b2[0][0]],
         [b2[8][1], b2[7][1], b2[6][1], b2[5][1], b2[4][1], b2[3][1], b2[2][1], b2[1][1], b2[0][1]],
         [b2[8][2], b2[7][2], b2[6][2], b2[5][2], b2[4][2], b2[3][2], b2[2][2], b2[1][2], b2[0][2]],
         [b2[8][3], b2[7][3], b2[6][3], b2[5][3], b2[4][3], b2[3][3], b2[2][3], b2[1][3], b2[0][3]],
         [b2[8][4], b2[7][4], b2[6][4], b2[5][4], b2[4][4], b2[3][4], b2[2][4], b2[1][4], b2[0][4]],
         [b2[8][5], b2[7][5], b2[6][5], b2[5][5], b2[4][5], b2[3][5], b2[2][5], b2[1][5], b2[0][5]],
         [b2[8][6], b2[7][6], b2[6][6], b2[5][6], b2[4][6], b2[3][6], b2[2][6], b2[1][6], b2[0][6]],
         [b2[8][7], b2[7][7], b2[6][7], b2[5][7], b2[4][7], b2[3][7], b2[2][7], b2[1][7], b2[0][7]],
         [b2[8][8], b2[7][8], b2[6][8], b2[5][8], b2[4][8], b2[3][8], b2[2][8], b2[1][8], b2[0][8]]],

        [[b2[8][8], b2[8][7], b2[8][6], b2[8][5], b2[8][4], b2[8][3], b2[8][2], b2[8][1], b2[8][0]],
         [b2[7][8], b2[7][7], b2[7][6], b2[7][5], b2[7][4], b2[7][3], b2[7][2], b2[7][1], b2[7][0]],
         [b2[6][8], b2[6][7], b2[6][6], b2[6][5], b2[6][4], b2[6][3], b2[6][2], b2[6][1], b2[6][0]],
         [b2[5][8], b2[5][7], b2[5][6], b2[5][5], b2[5][4], b2[5][3], b2[5][2], b2[5][1], b2[5][0]],
         [b2[4][8], b2[4][7], b2[4][6], b2[4][5], b2[4][4], b2[4][3], b2[4][2], b2[4][1], b2[4][0]],
         [b2[3][8], b2[3][7], b2[3][6], b2[3][5], b2[3][4], b2[3][3], b2[3][2], b2[3][1], b2[3][0]],
         [b2[2][8], b2[2][7], b2[2][6], b2[2][5], b2[2][4], b2[2][3], b2[2][2], b2[2][1], b2[2][0]],
         [b2[1][8], b2[1][7], b2[1][6], b2[1][5], b2[1][4], b2[1][3], b2[1][2], b2[1][1], b2[1][0]],
         [b2[0][8], b2[0][7], b2[0][6], b2[0][5], b2[0][4], b2[0][3], b2[0][2], b2[0][1], b2[0][0]]],

        [[b2[0][8], b2[1][8], b2[2][8], b2[3][8], b2[4][8], b2[5][8], b2[6][8], b2[7][8], b2[8][8]],
         [b2[0][7], b2[1][7], b2[2][7], b2[3][7], b2[4][7], b2[5][7], b2[6][7], b2[7][7], b2[8][7]],
         [b2[0][6], b2[1][6], b2[2][6], b2[3][6], b2[4][6], b2[5][6], b2[6][6], b2[7][6], b2[8][6]],
         [b2[0][5], b2[1][5], b2[2][5], b2[3][5], b2[4][5], b2[5][5], b2[6][5], b2[7][5], b2[8][5]],
         [b2[0][4], b2[1][4], b2[2][4], b2[3][4], b2[4][4], b2[5][4], b2[6][4], b2[7][4], b2[8][4]],
         [b2[0][3], b2[1][3], b2[2][3], b2[3][3], b2[4][3], b2[5][3], b2[6][3], b2[7][3], b2[8][3]],
         [b2[0][2], b2[1][2], b2[2][2], b2[3][2], b2[4][2], b2[5][2], b2[6][2], b2[7][2], b2[8][2]],
         [b2[0][1], b2[1][1], b2[2][1], b2[3][1], b2[4][1], b2[5][1], b2[6][1], b2[7][1], b2[8][1]],
         [b2[0][0], b2[1][0], b2[2][0], b2[3][0], b2[4][0], b2[5][0], b2[6][0], b2[7][0], b2[8][0]]],

        [[b2[0][8], b2[0][7], b2[0][6], b2[0][5], b2[0][4], b2[0][3], b2[0][2], b2[0][1], b2[0][0]],
         [b2[1][8], b2[1][7], b2[1][6], b2[1][5], b2[1][4], b2[1][3], b2[1][2], b2[1][1], b2[1][0]],
         [b2[2][8], b2[2][7], b2[2][6], b2[2][5], b2[2][4], b2[2][3], b2[2][2], b2[2][1], b2[2][0]],
         [b2[3][8], b2[3][7], b2[3][6], b2[3][5], b2[3][4], b2[3][3], b2[3][2], b2[3][1], b2[3][0]],
         [b2[4][8], b2[4][7], b2[4][6], b2[4][5], b2[4][4], b2[4][3], b2[4][2], b2[4][1], b2[4][0]],
         [b2[5][8], b2[5][7], b2[5][6], b2[5][5], b2[5][4], b2[5][3], b2[5][2], b2[5][1], b2[5][0]],
         [b2[6][8], b2[6][7], b2[6][6], b2[6][5], b2[6][4], b2[6][3], b2[6][2], b2[6][1], b2[6][0]],
         [b2[7][8], b2[7][7], b2[7][6], b2[7][5], b2[7][4], b2[7][3], b2[7][2], b2[7][1], b2[7][0]],
         [b2[8][8], b2[8][7], b2[8][6], b2[8][5], b2[8][4], b2[8][3], b2[8][2], b2[8][1], b2[8][0]]],

        [[b2[8][8], b2[7][8], b2[6][8], b2[5][8], b2[4][8], b2[3][8], b2[2][8], b2[1][8], b2[0][8]],
         [b2[8][7], b2[7][7], b2[6][7], b2[5][7], b2[4][7], b2[3][7], b2[2][7], b2[1][7], b2[0][7]],
         [b2[8][6], b2[7][6], b2[6][6], b2[5][6], b2[4][6], b2[3][6], b2[2][6], b2[1][6], b2[0][6]],
         [b2[8][5], b2[7][5], b2[6][5], b2[5][5], b2[4][5], b2[3][5], b2[2][5], b2[1][5], b2[0][5]],
         [b2[8][4], b2[7][4], b2[6][4], b2[5][4], b2[4][4], b2[3][4], b2[2][4], b2[1][4], b2[0][4]],
         [b2[8][3], b2[7][3], b2[6][3], b2[5][3], b2[4][3], b2[3][3], b2[2][3], b2[1][3], b2[0][3]],
         [b2[8][2], b2[7][2], b2[6][2], b2[5][2], b2[4][2], b2[3][2], b2[2][2], b2[1][2], b2[0][2]],
         [b2[8][1], b2[7][1], b2[6][1], b2[5][1], b2[4][1], b2[3][1], b2[2][1], b2[1][1], b2[0][1]],
         [b2[8][0], b2[7][0], b2[6][0], b2[5][0], b2[4][0], b2[3][0], b2[2][0], b2[1][0], b2[0][0]]],

        [[b2[8][0], b2[8][1], b2[8][2], b2[8][3], b2[8][4], b2[8][5], b2[8][6], b2[8][7], b2[8][8]],
         [b2[7][0], b2[7][1], b2[7][2], b2[7][3], b2[7][4], b2[7][5], b2[7][6], b2[7][7], b2[7][8]],
         [b2[6][0], b2[6][1], b2[6][2], b2[6][3], b2[6][4], b2[6][5], b2[6][6], b2[6][7], b2[6][8]],
         [b2[5][0], b2[5][1], b2[5][2], b2[5][3], b2[5][4], b2[5][5], b2[5][6], b2[5][7], b2[5][8]],
         [b2[4][0], b2[4][1], b2[4][2], b2[4][3], b2[4][4], b2[4][5], b2[4][6], b2[4][7], b2[4][8]],
         [b2[3][0], b2[3][1], b2[3][2], b2[3][3], b2[3][4], b2[3][5], b2[3][6], b2[3][7], b2[3][8]],
         [b2[2][0], b2[2][1], b2[2][2], b2[2][3], b2[2][4], b2[2][5], b2[2][6], b2[2][7], b2[2][8]],
         [b2[1][0], b2[1][1], b2[1][2], b2[1][3], b2[1][4], b2[1][5], b2[1][6], b2[1][7], b2[1][8]],
         [b2[0][0], b2[0][1], b2[0][2], b2[0][3], b2[0][4], b2[0][5], b2[0][6], b2[0][7], b2[0][8]]],

        [[b2[0][0], b2[1][0], b2[2][0], b2[3][0], b2[4][0], b2[5][0], b2[6][0], b2[7][0], b2[8][0]],
         [b2[0][1], b2[1][1], b2[2][1], b2[3][1], b2[4][1], b2[5][1], b2[6][1], b2[7][1], b2[8][1]],
         [b2[0][2], b2[1][2], b2[2][2], b2[3][2], b2[4][2], b2[5][2], b2[6][2], b2[7][2], b2[8][2]],
         [b2[0][3], b2[1][3], b2[2][3], b2[3][3], b2[4][3], b2[5][3], b2[6][3], b2[7][3], b2[8][3]],
         [b2[0][4], b2[1][4], b2[2][4], b2[3][4], b2[4][4], b2[5][4], b2[6][4], b2[7][4], b2[8][4]],
         [b2[0][5], b2[1][5], b2[2][5], b2[3][5], b2[4][5], b2[5][5], b2[6][5], b2[7][5], b2[8][5]],
         [b2[0][6], b2[1][6], b2[2][6], b2[3][6], b2[4][6], b2[5][6], b2[6][6], b2[7][6], b2[8][6]],
         [b2[0][7], b2[1][7], b2[2][7], b2[3][7], b2[4][7], b2[5][7], b2[6][7], b2[7][7], b2[8][7]],
         [b2[0][8], b2[1][8], b2[2][8], b2[3][8], b2[4][8], b2[5][8], b2[6][8], b2[7][8], b2[8][8]]]
    ])



# def n_i(i, j):
#     return str(i)
# def n_j(i, j):
#     return str(j)
# def r_i(i, j):
#     return str(8-i)
# def r_j(i, j):
#     return str(8-j)
#
# def board_print(f1, f2, prefix="b", suffix=""):
#     print("[", end="")
#     for i in range(9):
#         print("[", end="")
#         for j in range(9):
#             if j > 0:
#                 print(", ", end="")
#             print(prefix+"["+f1(i, j)+"]["+f2(i, j)+"]"+suffix, end="")
#         print("]"+("," if i < 8 else ""), end=("\n" if i < 8 else ""))
#     print("],", end="\n\n")
#
# board_print(n_i, n_j, prefix="f1(b", suffix=")")
# board_print(r_j, n_i, prefix="b1", suffix="")
# board_print(r_i, r_j, prefix="b1", suffix="")
# board_print(n_j, r_i, prefix="b1", suffix="")
#
# board_print(n_i, r_j, prefix="b1", suffix="")
# board_print(r_j, r_i, prefix="b1", suffix="")
# board_print(r_i, n_j, prefix="b1", suffix="")
# board_print(n_j, n_i, prefix="b1", suffix="")
#
# board_print(n_i, n_j, prefix="f2(b", suffix=")")
# board_print(r_j, n_i, prefix="b2", suffix="")
# board_print(r_i, r_j, prefix="b2", suffix="")
# board_print(n_j, r_i, prefix="b2", suffix="")
#
# board_print(n_i, r_j, prefix="b2", suffix="")
# board_print(r_j, r_i, prefix="b2", suffix="")
# board_print(r_i, n_j, prefix="b2", suffix="")
# board_print(n_j, n_i, prefix="b2", suffix="")
#
# b = [[P1, N, N, N, N, N, N, N, N],
#      [N, N, N, N, N, N, N, P2, N],
#      [N, N, P1, N, N, N, N, N, N],
#      [N, N, N, N, N, P2, N, N, N],
#      [N, N, N, N, P1, N, N, N, N],
#      [N, N, N, P2, N, N, N, N, N],
#      [N, N, N, N, N, N, P1, N, N],
#      [N, P2, N, N, N, N, N, N, N],
#      [N, N, N, N, N, N, N, N, P1]]
#
# start = datetime.datetime.utcnow()
# for _ in range(1000000):
#     a = [[f1(b[i][j]) for i in range(9)] for j in range(9)]
# end = datetime.datetime.utcnow()
# print(end-start)
# start = datetime.datetime.utcnow()
# for _ in range(1000000):
#     a = [[f1(b[0][0]), f1(b[0][1]), f1(b[0][2]), f1(b[0][3]), f1(b[0][4]), f1(b[0][5]), f1(b[0][6]), f1(b[0][7]), f1(b[0][8])],
#          [f1(b[1][0]), f1(b[1][1]), f1(b[1][2]), f1(b[1][3]), f1(b[1][4]), f1(b[1][5]), f1(b[1][6]), f1(b[1][7]), f1(b[1][8])],
#          [f1(b[2][0]), f1(b[2][1]), f1(b[2][2]), f1(b[2][3]), f1(b[2][4]), f1(b[2][5]), f1(b[2][6]), f1(b[2][7]), f1(b[2][8])],
#          [f1(b[3][0]), f1(b[3][1]), f1(b[3][2]), f1(b[3][3]), f1(b[3][4]), f1(b[3][5]), f1(b[3][6]), f1(b[3][7]), f1(b[3][8])],
#          [f1(b[4][0]), f1(b[4][1]), f1(b[4][2]), f1(b[4][3]), f1(b[4][4]), f1(b[4][5]), f1(b[4][6]), f1(b[4][7]), f1(b[4][8])],
#          [f1(b[5][0]), f1(b[5][1]), f1(b[5][2]), f1(b[5][3]), f1(b[5][4]), f1(b[5][5]), f1(b[5][6]), f1(b[5][7]), f1(b[5][8])],
#          [f1(b[6][0]), f1(b[6][1]), f1(b[6][2]), f1(b[6][3]), f1(b[6][4]), f1(b[6][5]), f1(b[6][6]), f1(b[6][7]), f1(b[6][8])],
#          [f1(b[7][0]), f1(b[7][1]), f1(b[7][2]), f1(b[7][3]), f1(b[7][4]), f1(b[7][5]), f1(b[7][6]), f1(b[7][7]), f1(b[7][8])],
#          [f1(b[8][0]), f1(b[8][1]), f1(b[8][2]), f1(b[8][3]), f1(b[8][4]), f1(b[8][5]), f1(b[8][6]), f1(b[8][7]), f1(b[8][8])]]
#     end = datetime.datetime.utcnow()
# print(end-start)