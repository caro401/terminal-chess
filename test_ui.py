import unittest
import chess


class TestUiDrawing(unittest.TestCase):
    def test_draw_empty_board(self):
        self.assertEqual(chess.render_board(), '_ _ _ _ _ _ _ _\n' * 8)


if __name__ == '__main__':
    unittest.main()
