import unittest
import chess

WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'


class TestPawnMoves(unittest.TestCase):
    def setUp(self):
        self.test_board = chess.Board(False)
        self.test_board.board = [[WR, WN, WB, WQ, WK, WB, WN, WR], [WP, WP, WP, WP, None, None, WP, WP],
                                 [None, None, BP, None, None, WP, None, None],
                                 [None, None, None, None, None, BN, None, None],
                                 [None, None, None, None, WP, None, BP, None],
                                 [None, None, None, BP, None, None, None, None],
                                 [BP, BP, None, None, BP, BP, None, BP], [BR, BN, BB, BQ, BK, BB, None, BR]]
        # print(self.test_board.render_board())

    def test_white_pawn_initial(self):
        self.assertEqual(self.test_board.get_valid_moves(1, 0), set([(2, 0), (3, 0)]))

    def test_black_pawn_initial(self):
        self.assertEqual(self.test_board.get_valid_moves(6, 0), set([(5, 0), (4, 0)]))

    def test_white_pawn_general(self):
        self.assertEqual(self.test_board.get_valid_moves(2, 5), set())

    def test_black_pawn_general(self):
        self.assertEqual(self.test_board.get_valid_moves(4, 6), set([(3, 6)]))

    def test_white_pawn_take_initial(self):
        self.assertEqual(self.test_board.get_valid_moves(1, 3), set([(2, 2), (2, 3), (3, 3)]))

    def test_black_pawn_take(self):
        self.assertEqual(self.test_board.get_valid_moves(5, 3), set([(4, 3), (4, 4)]))

    # @unittest.expectedFailure
    def test_black_en_passant(self):
        pass

    # @unittest.expectedFailure
    def test_white_en_passant(self):
        pass


class TestKnightMoves(unittest.TestCase):
    def setUp(self):
        self.test_board = chess.Board(False)
        self.test_board.board = [[WR, None, WB, WQ, WK, WB, None, WR], [WP, WP, WP, WP, None, None, WP, WP],
                                 [None, None, BP, None, None, WP, None, WN],
                                 [None, None, WN, None, None, BN, None, None],
                                 [None, None, None, None, WP, None, BP, None],
                                 [None, None, None, BP, None, None, None, None],
                                 [BP, BP, None, None, BP, BP, None, BP], [BR, BN, BB, BQ, BK, BB, None, BR]]
        # print(self.test_board.render_board())

    def test_black_knight_initial(self):
        self.assertEqual(self.test_board.get_valid_moves(7, 1), set([(5, 0), (5, 2), (6, 3)]))

    def test_white_knight_blocked(self):
        self.assertEqual(self.test_board.get_valid_moves(3, 2), set([(4, 0), (5, 1), (5, 3), (2, 4), (2, 0)]))

    def test_black_knight(self):
        self.assertEqual(self.test_board.get_valid_moves(3, 5),
                         set([(1, 4), (2, 3), (4, 3), (5, 4), (5, 6), (4, 7), (2, 7), (1, 6)]))

    def test_white_knight_edge(self):
        self.assertEqual(self.test_board.get_valid_moves(2, 7), set([(0, 6), (1, 5), (3, 5), (4, 6)]))

if __name__ == '__main__':
    unittest.main()