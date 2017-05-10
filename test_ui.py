import unittest
from chess import ChessGame

WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'


class TestUiDrawing(unittest.TestCase):
    def setUp(self):
        self.game = ChessGame(False)

    def test_draw_empty_board(self):
        row = [None] * 8
        self.game.board.board_list = [row] * 8
        self.assertEqual(self.game.render_board(), '_ _ _ _ _ _ _ _ \n' * 8)

    def test_draw_start_board(self):
        start_board = """♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n\
_ _ _ _ _ _ _ _ \n_ _ _ _ _ _ _ _ \n_ _ _ _ _ _ _ _ \n_ _ _ _ _ _ _ _ \n\
♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 
"""
        self.assertEqual(self.game.render_board(), start_board)

    def test_draw_board_axes(self):
        self.game.axes = True
        row = [None] * 8
        self.game.board.board_list = [row] * 8
        axes_board = 'a b c d e f g h  \n'
        for i in range(8, 0, -1):
            axes_board += f'_ _ _ _ _ _ _ _ {i}\n'
        self.assertEqual(self.game.render_board(), axes_board)

    def test_move_parser(self):
        self.assertIsNone(self.game.parse_move('z9 b3'))
        self.assertIsNone(self.game.parse_move('do a move now'))
        self.assertEqual(self.game.parse_move('a3 a4'), ((2, 0), (3, 0)))
        self.assertEqual(self.game.parse_move('f2 e4'), ((1, 5), (3, 4)))


if __name__ == '__main__':
    unittest.main()
