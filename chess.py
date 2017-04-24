WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'


class Board:
    def __init__(self, axes):
        self.board = [[WR, WN, WB, WQ, WK, WB, WN, WR], [WP] * 8,  [None] * 8, [None] * 8,
                      [None] * 8, [None] * 8, [BP] * 8, [BR, BN, BB, BQ, BK, BB, BN, BR]]
        self.axes = axes

    def update_board(self):
        print(self.render_board())

    def render_board(self):
        # draw board as a string, given array of pieces
        board_str = ''
        if self.axes:
            board_str += 'a b c d e f g h  \n'
        for i in range(7, -1, -1):
            for piece in self.board[i]:
                if piece:
                    board_str += f'{piece} '
                else:
                    board_str += '_ '
            if self.axes:
                board_str += str(i + 1)
            board_str += '\n'
        return board_str


if __name__ == '__main__':
    gameboard = Board(True)
    gameboard.update_board()
