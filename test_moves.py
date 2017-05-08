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
        self.assertEqual(self.test_board.get_valid_moves(1, 0), {(2, 0), (3, 0)})

    def test_black_pawn_initial(self):
        self.assertEqual(self.test_board.get_valid_moves(6, 0), {(5, 0), (4, 0)})

    def test_white_pawn_general(self):
        self.assertEqual(self.test_board.get_valid_moves(2, 5), set())

    def test_black_pawn_general(self):
        self.assertEqual(self.test_board.get_valid_moves(4, 6), {(3, 6)})

    def test_white_pawn_take_initial(self):
        self.assertEqual(self.test_board.get_valid_moves(1, 3), {(2, 2), (2, 3), (3, 3)})

    def test_black_pawn_take(self):
        self.assertEqual(self.test_board.get_valid_moves(5, 3), {(4, 3), (4, 4)})

    # @unittest.expectedFailure
    def test_black_en_passant(self):
        # TODO write en passant tests
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
        self.assertEqual(self.test_board.get_valid_moves(7, 1), {(5, 0), (5, 2), (6, 3)})

    def test_white_knight_blocked(self):
        self.assertEqual(self.test_board.get_valid_moves(3, 2), {(4, 0), (5, 1), (5, 3), (2, 4), (2, 0)})

    def test_black_knight(self):
        self.assertEqual(self.test_board.get_valid_moves(3, 5),
                         {(1, 4), (2, 3), (4, 3), (5, 4), (5, 6), (4, 7), (2, 7), (1, 6)})

    def test_white_knight_edge(self):
        self.assertEqual(self.test_board.get_valid_moves(2, 7), {(0, 6), (1, 5), (3, 5), (4, 6)})


class TestBishopMoves(unittest.TestCase):
    def setUp(self):
        self.test_board = chess.Board(False)
        self.test_board.board = [[WR, None, None, WQ, WK, WB, None, WR], [WP, WP, WP, WP, None, None, WP, WP],
                                 [None, None, BP, None, None, WP, None, WN],
                                 [None, None, WN, None, None, BN, None, None],
                                 [WB, None, None, BB, WP, None, BP, None],
                                 [None, None, None, BP, None, None, None, None],
                                 [BP, BP, None, None, BP, BP, None, BP], [BR, BN, BB, BQ, BK, None, None, BR]]
        # print(self.test_board.render_board())

    def test_black_bishop_initial(self):
        self.assertEqual(self.test_board.get_valid_moves(7, 2), {(6, 3), (5, 4), (4, 5), (3, 6), (2, 7)})

    def test_white_bishop_initial(self):
        self.assertEqual(self.test_board.get_valid_moves(0, 5), {(1, 4), (2, 3)})

    def test_white_bishop(self):
        self.assertEqual(self.test_board.get_valid_moves(4, 0), {(5, 1), (6, 2), (7, 3), (3, 1), (2, 2)})

    def test_black_bishop(self):
        self.assertEqual(self.test_board.get_valid_moves(4, 3), {(5, 2), (5, 4), (3, 2), (3, 4), (2, 5)})


class TestRookMoves(unittest.TestCase):
    def setUp(self):
        self.test_board = chess.Board(False)
        self.test_board.board = [[WR, None, None, WQ, WK, WB, None, WR], [None, WP, WP, WP, None, None, WP, WP],
                                 [BN, None, BP, None, None, WP, None, WN],
                                 [WP, None, WN, None, None, None, None, None],
                                 [WB, None, None, BR, WP, None, BP, None],
                                 [None, None, None, BP, None, None, None, None],
                                 [BP, BP, None, None, BP, BP, None, BP], [BR, BN, BB, BQ, BK, BB, None, None]]
        # print(self.test_board.render_board())

    def test_black_rook(self):
        self.assertEqual(self.test_board.get_valid_moves(4, 3),
                         {(4, 2), (4, 1), (4, 0), (4, 4), (3, 3), (2, 3), (1, 3)})

    def test_white_rook(self):
        self.assertEqual(self.test_board.get_valid_moves(0, 0), {(1, 0), (2, 0), (0, 1), (0, 2)})


class TestQueenMoves(unittest.TestCase):
    def setUp(self):
        self.test_board = chess.Board(False)
        self.test_board.board = [[WR, None, None, None, WK, WB, None, WR], [None, WP, WP, WP, None, None, WP, WP],
                                 [BN, None, BP, None, None, WP, None, WN],
                                 [WP, None, WN, WQ, None, None, None, None],
                                 [WB, None, None, None, WP, None, BP, None],
                                 [None, None, BQ, BP, None, None, None, None],
                                 [BP, BP, None, None, BP, BP, None, BP], [BR, BN, BB, None, BK, BB, None, BR]]
        # print(self.test_board.render_board())

    def test_black_queen(self):
        self.assertEqual(self.test_board.get_valid_moves(5, 2),
                         {(5, 1), (5, 0), (6, 2), (6, 3), (4, 3), (3, 4), (2, 5), (4, 2), (3, 2), (4, 1), (3, 0)})

    def test_white_queen(self):
        self.assertEqual(self.test_board.get_valid_moves(3, 3),
                         {(4, 2), (5, 1), (6, 0), (4, 3), (5, 3), (3, 4), (3, 5),
                          (3, 6), (3, 7), (2, 4), (1, 5), (0, 6), (2, 3), (2, 2)})


if __name__ == '__main__':
    unittest.main()
