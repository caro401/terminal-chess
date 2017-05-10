from board import Board
from glb import *
from typing import Set
from copy import deepcopy
import re


class ChessGame:
    def __init__(self, show_axes=True):
        self.board = Board()
        self.axes = show_axes
        self.white_move = True

    def display_valid_moves(self, row: int, col: int) -> None:
        # hint what moves the piece can make
        moves_set: Set[Coordinates] = self.board.get_valid_moves(row, col)
        show: BoardList = deepcopy(self.board.board_list)
        for location in moves_set:
            show[location[0]][location[1]] = 'x'
        print(self.render_board(show))

    def parse_move(self, move_str: str) -> Optional[Coordinates]:
        # expect move in form 'a8 a4' - move piece on grid ref a8 to a4
        # or 'a4?' - what's the valid moves for the piece on a4?
        if not re.match(r'[a-h][1-8] [a-h][1-8]', move_str):
            if re.match(r'[a-h][1-8]\?', move_str):
                x: int = int(move_str[1]) - 1
                y: int = COLS_MAP[move_str[0]]
                if self.board.board_list[x][y]:
                    self.display_valid_moves(int(move_str[1]) - 1, COLS_MAP[move_str[0]])
                else:
                    print('No piece there...')
            else:
                print('Invalid move command, please try again')
            return None
        origin, target = move_str.split(' ')
        return (int(origin[1]) - 1, COLS_MAP[origin[0]]), (int(target[1]) - 1, COLS_MAP[target[0]])

    def update_board(self, move_str=None) -> None:
        # given a user's move, update the game board
        if move_str:
            move = self.parse_move(move_str)
            if move:
                origin, target = move
                if self.white_move and (self.board.board_list[origin[0]][origin[1]] not in WHITE_PIECES):
                    print("White move, you can't move that piece")
                elif (not self.white_move) and (self.board.board_list[origin[0]][origin[1]] not in BLACK_PIECES):
                    print("White move, you can't move that piece")
                else:
                    valid_moves: Set[Coordinates] = self.board.get_valid_moves(origin[0], origin[1])
                    if target in valid_moves:
                        self.board.make_move(origin, target)
                        self.white_move = not self.white_move
                    else:
                        print('You can\'t move that piece to there')
        else:
            print('No move made')
        print(self.render_board())

    def render_board(self, draw_board=None) -> str:
        # draw board as a string, given array of pieces
        if not draw_board:
            draw_board: BoardList = self.board.board_list
        board_str: str = ''
        if self.axes:
            board_str += 'a b c d e f g h  \n'
        for i in range(7, -1, -1):
            for piece in draw_board[i]:
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
    game = ChessGame()
    enter_move = None
    while enter_move != 'quit':
        game.update_board(enter_move)
        enter_move = input('Your move: ')
