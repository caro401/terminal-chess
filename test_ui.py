import unittest
import chess

WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'


class TestUiDrawing(unittest.TestCase):
    def setUp(self):
        self.test_board = chess.Board(False)

    def test_draw_empty_board(self):
        row = [None] * 8
        self.test_board.board = [row] * 8
        self.assertEqual(self.test_board.render_board(), '_ _ _ _ _ _ _ _ \n' * 8)

    def test_draw_start_board(self):
        start_board = """♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n\
_ _ _ _ _ _ _ _ \n_ _ _ _ _ _ _ _ \n_ _ _ _ _ _ _ _ \n_ _ _ _ _ _ _ _ \n\
♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ 
"""
        self.assertEqual(self.test_board.render_board(), start_board)

    def test_draw_board_axes(self):
        self.test_board.axes = True
        row = [None] * 8
        self.test_board.board = [row] * 8
        axes_board = 'a b c d e f g h  \n'
        for i in range(8, 0, -1):
            axes_board += f'_ _ _ _ _ _ _ _ {i}\n'
        self.assertEqual(self.test_board.render_board(), axes_board)


if __name__ == '__main__':
    unittest.main()
