import re
import moves
import copy

WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'
MOVES_MAP = {WP: moves.white_pawn_move, BP: moves.black_pawn_move, BR: moves.rook_move, WR: moves.rook_move,
             WB: moves.bishop_move, BB: moves.bishop_move, WQ: moves.queen_move, BQ: moves.queen_move,
             WN: moves.knight_move, BN: moves.knight_move, WK: moves.king_move, BK: moves.king_move}


class Board:
    def __init__(self, axes):
        self.board = [[WR, WN, WB, WQ, WK, WB, WN, WR], [WP] * 8,  [None] * 8, [None] * 8,
                      [None] * 8, [None] * 8, [BP] * 8, [BR, BN, BB, BQ, BK, BB, BN, BR]]
        self.axes = axes

    def update_board(self, move_str=None):
        # given a user's move, update the game board
        if move_str:
            move = self.parse_move(move_str)
            if move:
                origin, target = move
                valid_moves = self.get_valid_moves(origin[0], origin[1])
                if target in valid_moves:
                    self.board[target[0]][target[1]], self.board[origin[0]][origin[1]] =\
                        self.board[origin[0]][origin[1]], None
                else:
                    print('You can\'t move that piece to there')
        else:
            print('No move made')
        print(self.render_board())

    def parse_move(self, move_str):
        # expect move in form 'a8 a4' - move piece on grid ref a8 to a4
        cols_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        if not re.match(r'[a-h][1-8] [a-h][1-8]', move_str):
            if re.match(r'[a-h][1-8]\?', move_str):
                self.display_valid_moves(int(move_str[1]) - 1, cols_map[move_str[0]])
            else:
                print('Invalid move command, please try again')
            return None
        origin, target = move_str.split(' ')
        return (int(origin[1]) - 1, cols_map[origin[0]]), (int(target[1]) - 1, cols_map[target[0]])

    def display_valid_moves(self, row, col):
        moves_set = self.get_valid_moves(row, col)
        show = copy.deepcopy(self.board)
        for location in moves_set:
            show[location[0]][location[1]] = 'x'
        print(self.render_board(show))

    def get_valid_moves(self, row, col):
        return MOVES_MAP[self.board[row][col]]((row, col), self.board)

    def render_board(self, board=None):
        # draw board as a string, given array of pieces
        if not board:
            board = self.board
        board_str = ''
        if self.axes:
            board_str += 'a b c d e f g h  \n'
        for i in range(7, -1, -1):
            for piece in board[i]:
                if piece:
                    board_str += f'{piece} '
                else:
                    board_str += '_ '
            if self.axes:
                board_str += str(i + 1)
            board_str += '\n'
        return board_str


if __name__ == '__main__':
    print('\tPlay chess! Type your moves as "a2 a4" - move piece on a2 to a4\n\
    \tor query where you can move with "a2?"\n\tType "quit" to stop\n\
\tThere are no rules enforced yet!')
    gameboard = Board(True)
    move = None
    while move != 'quit':
        gameboard.update_board(move)
        move = input('Your move: ')
