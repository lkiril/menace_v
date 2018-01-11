class Board:
    def __init__(self, init_vector):
        self.board = init_vector


    def rf(self, isFlip, numRotate):
        return self.rotate_and_flip(self.board, isFlip, numRotate)


    @staticmethod
    def rotate_and_flip(board, isFlip, numRotate):
        temp_board_f = list(board)
        if isFlip:
            temp_board_f[0] = board[2]
            temp_board_f[2] = board[0]
            temp_board_f[3] = board[5]
            temp_board_f[5] = board[3]
            temp_board_f[6] = board[8]
            temp_board_f[8] = board[6]

        temp_board_r = list(temp_board_f)
        for i in xrange(numRotate):
            temp_board_r[0] = temp_board_f[2]
            temp_board_r[1] = temp_board_f[5]
            temp_board_r[2] = temp_board_f[8]
            temp_board_r[3] = temp_board_f[1]
            temp_board_r[5] = temp_board_f[7]
            temp_board_r[6] = temp_board_f[0]
            temp_board_r[7] = temp_board_f[3]
            temp_board_r[8] = temp_board_f[6]

            temp_board_f = list(temp_board_r)

        return temp_board_r

    def make_move(self, player, position):
        if player not in [1,2]:
            raise Exception("Invalid player")
        if position not in range(9):
            raise Exception("Invalid move")
        if self.board[position] != 0:
            raise Exception("Position not empty")

        self.board[position] = player

    def is_game_over(self):
        if self.board[0] != 0 and self.board[0] == self.board[1] == self.board[2]:
            return self.board[0]
        if self.board[3] != 0 and self.board[3] == self.board[4] == self.board[5]:
            return self.board[3]
        if self.board[6] != 0 and self.board[6] == self.board[7] == self.board[8]:
            return self.board[6]
        if self.board[0] != 0 and self.board[0] == self.board[3] == self.board[6]:
            return self.board[0]
        if self.board[1] != 0 and self.board[1] == self.board[4] == self.board[7]:
            return self.board[1]
        if self.board[2] != 0 and self.board[2] == self.board[5] == self.board[8]:
            return self.board[2]
        if self.board[0] != 0 and self.board[0] == self.board[4] == self.board[8]:
            return self.board[0]
        if self.board[2] != 0 and self.board[2] == self.board[4] == self.board[6]:
            return self.board[2]
        return 0

    def check_board(self, other):
        for f in [0,1]:
            for r in [0, 1, 2, 3]:
                if other.rf(f, r) == self.board:
                    return (f, r), True
        return (-1,-1), False

    def get_status(self):
        return self.board

    def __str__(self):
        return str(self.board)