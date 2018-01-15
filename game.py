from params import *
from board import Board
import log
import time
import random


class Game:

    def __init__(self):
        self.all_boards = self.init_boards()
        self.gid = int(time.time())
        self.board = Board([0,0,0,0,0,0,0,0,0])
        self.current_player = 1

    def debug(self, board_num):
        print self.all_boards[board_num]

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
        return None, None

    def get_status(self):
        res = {}
        res['gid'] = self.gid
        res['board'] = self.board.get_status()
        res['matchbox'], res['colors'] = self.get_matchbox()
        winner = self.board.winner()
        if winner > 0:
            res['instructions'] = self.get_end_game_instructions(winner)
            if winner == 1:
                res['quote'] = random.choice(QUOTES)
        res['gameover'] = winner
        res['current_player'] = self.current_player
        res['log'] = log.get(self.gid)

        return res

    def get_end_game_instructions(self, winner):
        game_logs = log.get(self.gid)
        instructions = []
        msg = ""
        if winner == 1:
            msg = "return the played color {0} to matchbox {1} and put 3 more similar beads"
        if winner == 2:
            msg = "take the played color {0} from matchbox {1}"
        if winner == 3:
            msg = "return the played color {0} to matchbox {1} and put 1 more similar bead"
        for turn_log in game_logs:
            if '1' in turn_log and 'mb' in turn_log:
                instructions.append(msg.format(turn_log['1'], turn_log['mb']))
        return instructions

    def make_move(self, player, position):
        self.board.make_move(player, position)

    def is_game_over(self):
        return self.board.is_game_over()

    def make_menace_move(self, position):
        if self.current_player != 1:
            raise Exception("wrong player")
        self.board.check_valid_move(1, position)

        i, color = self.get_matchbox()

        log.write(self.gid, {"mb": i, 1: position})

        self.make_move(1, position)
        self.current_player = 2



    def make_player_move(self, position):
        if self.current_player != 2:
            raise Exception("wrong player")
        self.board.check_valid_move(1, position)

        log.write(self.gid, {2: position})

        self.make_move(2, position)
        self.current_player = 1

if __name__ == '__main__':
    g = Game()
    print g.debug(301)