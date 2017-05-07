import re
import moves
import copy

# TODO custom type for board list thing

COLS_MAP = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'
BLACK_PIECES = frozenset([BK, BQ, BR, BB, BN, BP])
WHITE_PIECES = frozenset([WK, WQ, WR, WB, WN, WP])
MOVES_MAP = {WP: moves.white_pawn_move, BP: moves.black_pawn_move, BR: moves.rook_move, WR: moves.rook_move,
             WB: moves.bishop_move, BB: moves.bishop_move, WQ: moves.queen_move, BQ: moves.queen_move,
             WN: moves.knight_move, BN: moves.knight_move, WK: moves.king_move, BK: moves.king_move}


class Board:
    def __init__(self, axes: bool) -> None:
        self.board: list = [[WR, WN, WB, WQ, WK, WB, WN, WR], [WP] * 8,  [None] * 8, [None] * 8,
                            [None] * 8, [None] * 8, [BP] * 8, [BR, BN, BB, BQ, BK, BB, BN, BR]]
        self.axes: bool = axes
        self.white_move: bool = True

    def update_board(self, move_str=None) -> None:
        # given a user's move, update the game board
        if move_str:
            move = self.parse_move(move_str)
            if move:
                origin, target = move
                if self.white_move and (self.board[origin[0]][origin[1]] not in WHITE_PIECES):
                    print("White move, you can't move that piece")
                elif (not self.white_move) and (self.board[origin[0]][origin[1]] not in BLACK_PIECES):
                    print("White move, you can't move that piece")
                else:
                    valid_moves: set = self.get_valid_moves(origin[0], origin[1])
                    if target in valid_moves:
                        self.board[target[0]][target[1]], self.board[origin[0]][origin[1]] =\
                            self.board[origin[0]][origin[1]], None
                        self.white_move = not self.white_move
                    else:
                        print('You can\'t move that piece to there')
        else:
            print('No move made')
        print(self.render_board())

    def parse_move(self, move_str: str):
        # expect move in form 'a8 a4' - move piece on grid ref a8 to a4
        # or 'a4?' - what's the valid moves for the piece on a4?
        if not re.match(r'[a-h][1-8] [a-h][1-8]', move_str):
            if re.match(r'[a-h][1-8]\?', move_str):
                x: int = int(move_str[1]) - 1
                y: int = COLS_MAP[move_str[0]]
                if self.board[x][y]:
                    self.display_valid_moves(int(move_str[1]) - 1, COLS_MAP[move_str[0]])
                else:
                    print('No piece there...')
            else:
                print('Invalid move command, please try again')
            return None
        origin, target = move_str.split(' ')
        return (int(origin[1]) - 1, COLS_MAP[origin[0]]), (int(target[1]) - 1, COLS_MAP[target[0]])

    def display_valid_moves(self, row: int, col: int) -> None:
        moves_set: set = self.get_valid_moves(row, col)
        show: list = copy.deepcopy(self.board)
        for location in moves_set:
            show[location[0]][location[1]] = 'x'
        print(self.render_board(show))

    def get_valid_moves(self, row: int, col: int) -> set:
        return MOVES_MAP[self.board[row][col]]((row, col), self.board)

    def render_board(self, board=None)-> str:
        # draw board as a string, given array of pieces
        if not board:
            board: list = self.board
        board_str: str = ''
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
    \tor query where you can move with "a2?"\n\tType "quit" to stop\n')
    gameboard: Board = Board(True)
    enter_move = None
    while enter_move != 'quit':
        gameboard.update_board(enter_move)
        enter_move = input('Your move: ')
