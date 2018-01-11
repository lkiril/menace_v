from params import *
from board import Board


class Game:

    def __init__(self):
        self.all_boards = self.init_boards()
        self.board = Board([0,0,0,0,0,0,0,0,0])

    def init_boards(self):

        boards = []
        for i in xrange(0, len(BOARD_INPUTS) - 1, 9):
            b = Board(BOARD_INPUTS[i:i + 9])
            boards.append(b)
        return boards

    def get_matchbox(self):
        for i, board in enumerate(self.all_boards):
            (f,r), res = self.board.check_board(board)
            if res:
                colors = Board.rotate_and_flip([0,1,2,3,4,5,6,7,8], f, r)
                return i, colors
        return -1, None

    def get_status(self):
        res = {}
        res['board'] = self.board.get_status()
        res['matchbox'], res['colors'] = self.get_matchbox()
        res['gameover'] = self.board.is_game_over()
        return res

    def make_move(self, player, position):
        self.board.make_move(player, position)

    def is_game_over(self):
        return self.board.is_game_over()

    def make_menace_move(self, position):
        self.make_move(1, position)

    def make_player_move(self, position):
        self.make_move(2, position)

        mb = self.get_matchbox()
        print mb[0], position



#g = Game()

# g.make_menace_move(4)
# g.make_player_move(8)
# g.make_menace_move(5)
# g.make_player_move(2)
# g.make_menace_move(3)



# def init_game():
#     self.all_boards = init_boards()
# boards = init_boards()
#
# #test_board = Board([1, 2, 0, 0, 0, 0, 0, 0, 0])
# test_board = Board([0, 0, 1,
#                     1, 0, 2,
#                     2, 2, 1])
#
# # for f in [0, 1]:
# #     for r in [0, 1, 2, 3]:
# #         print test_board.rf(f, r)
#
# for b in boards:
#     if b == test_board:
#         print "horray!", b
