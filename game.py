from params import *
from board import Board
import log
import time
import random
import matplotlib.pyplot as plt


class Game:

    def __init__(self):
        self.all_boards = self.init_boards()
        self.gid = int(time.time())
        self.board = Board([0,0,0,0,0,0,0,0,0])
        self.current_player = 1
        stats_sum = 0
        stats = []
        for s in log.get_stats():
            stats.append(stats_sum)
            stats_sum += int(s)
        stats.append(stats_sum)
        self.save_chart(stats)

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
                res['quote'] = random.choice(WIN_QUOTES)
            elif winner == 2:
                res['quote'] = random.choice(LOSE_QUOTES)
            elif winner == 3:
                res['quote'] = random.choice(DRAW_QUOTES)
        res['gameover'] = winner
        res['current_player'] = self.current_player
        res['log'] = log.get(self.gid)

        return res

    def get_end_game_instructions(self, winner):
        game_logs = log.get(self.gid)
        instructions = []
        msg = ""
        num = ""
        if winner == 1:
            msg = "Add 3 {0} beads to matchbox #{1} "
            num = 3
            log.write_stats(3)
        if winner == 2:
            msg = "Remove 1 {0} bead from matchbox #{1}"
            num = -1
            log.write_stats(-1)
        if winner == 3:
            msg = "Add 1 {0} bead to matchbox #{1}"
            num = 1
            log.write_stats(1)
        for turn_log in game_logs:
            if '1' in turn_log and 'mb' in turn_log:
                instructions.append({
                    'msg': msg.format(COLORS[turn_log['color']], turn_log['mb']),
                    'num': num,
                    'color': turn_log['color']
                })
        return instructions

    def make_move(self, player, position):
        self.board.make_move(player, position)

    def is_game_over(self):
        return self.board.winner() != 0

    def make_menace_move(self, position):
        if self.current_player != 1:
            raise Exception("wrong player")
        self.board.check_valid_move(1, position)

        i, color = self.get_matchbox()

        if i is not None:
            log.write(self.gid, {"mb": i, 1: position, "color": color[position]})

        self.make_move(1, position)
        self.current_player = 2

    def make_player_move(self, position):
        if self.current_player != 2:
            raise Exception("wrong player")
        self.board.check_valid_move(1, position)

        log.write(self.gid, {2: position})

        self.make_move(2, position)
        self.current_player = 1

        self.last_move()

    def last_move(self):
        if self.is_game_over():
            return
        move = self.board.last_move()
        if move == -1:
            return
        self.make_menace_move(move)

    def save_chart(self, results):
        plt.plot(results, "r.-")
        plt.xlabel("Games played")
        plt.ylabel("Menace performance")
        plt.title("How smart is Menace?")
        plt.savefig("static/chart.png")


if __name__ == '__main__':
    g = Game()
    print g.debug(301)
