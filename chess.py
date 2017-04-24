import re

WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'
black_pieces = frozenset([BK, BQ, BR, BB, BN, BP])
white_pieces = frozenset([WK, WQ, WR, WB, WN, WP])


class Board:
    def __init__(self, axes):
        self.board = [[WR, WN, WB, WQ, WK, WB, WN, WR], [WP] * 8,  [None] * 8, [None] * 8,
                      [None] * 8, [None] * 8, [BP] * 8, [BR, BN, BB, BQ, BK, BB, BN, BR]]
        self.axes = axes

    def update_board(self, move_str=None):
        # given a user's move, update the game board
        if move_str:
            if self.parse_move(move_str):
                origin, target = self.parse_move(move_str)
                self.board[target[0]][target[1]], self.board[origin[0]][origin[1]] =\
                    self.board[origin[0]][origin[1]], None
        else:
            print('No move made')
        print(self.render_board())

    @staticmethod
    def parse_move(move_str):  
        # expect move in form 'a8 a4' - move piece on grid ref a8 to a4
        cols_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        if not re.match(r'[a-h][1-8] [a-h][1-8]', move_str):
            print('Invalid move command, please try again')
            return None
        origin, target = move_str.split(' ')
        return (int(origin[1]) - 1, cols_map[origin[0]]), (int(target[1]) - 1, cols_map[target[0]])

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
    print('\tPlay chess! Type your moves as "a2 a4" - move piece on a2 to a4\n\tType "quit" to stop\n\
\tThere are no rules enforced yet!')
    gameboard = Board(True)
    move = None
    while move != 'quit':
        gameboard.update_board(move)
        move = input('Your move: ')
