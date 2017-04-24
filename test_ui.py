import unittest
import chess

WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'


class TestUiDrawing(unittest.TestCase):
    def test_draw_empty_board(self):
        self.assertEqual(chess.render_board([None]), '_ _ _ _ _ _ _ _\n' * 8)

    def test_draw_start_board(self):
        start_board = """♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜
♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _
♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙
♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖
"""
        self.assertEqual(chess.render_board(), start_board)


if __name__ == '__main__':
    unittest.main()
