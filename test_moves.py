import unittest
from board import Board

xx = None
WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'


class TestPawnMoves(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()
        self.test_board.board_list = [[WR, WN, WB, WQ, WK, WB, WN, WR],
                                      [WP, WP, WP, WP, xx, xx, WP, WP],
                                      [xx, xx, BP, xx, xx, WP, xx, xx],
                                      [xx, xx, xx, xx, xx, BN, xx, xx],
                                      [xx, xx, xx, xx, WP, xx, BP, xx],
                                      [xx, xx, xx, BP, xx, xx, xx, xx],
                                      [BP, BP, xx, xx, BP, BP, xx, BP],
                                      [BR, BN, BB, BQ, BK, BB, xx, BR]]

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
        self.test_board = Board()
        self.test_board.board_list = [[WR, xx, WB, WQ, WK, WB, xx, WR],
                                      [WP, WP, WP, WP, xx, xx, WP, WP],
                                      [xx, xx, BP, xx, xx, WP, xx, WN],
                                      [xx, xx, WN, xx, xx, BN, xx, xx],
                                      [xx, xx, xx, xx, WP, xx, BP, xx],
                                      [xx, xx, xx, BP, xx, xx, xx, xx],
                                      [BP, BP, xx, xx, BP, BP, xx, BP],
                                      [BR, BN, BB, BQ, BK, BB, xx, BR]]

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
        self.test_board = Board()
        self.test_board.board_list = [[WR, xx, xx, WQ, WK, WB, xx, WR],
                                      [WP, WP, WP, WP, xx, xx, WP, WP],
                                      [xx, xx, BP, xx, xx, WP, xx, WN],
                                      [xx, xx, WN, xx, xx, BN, xx, xx],
                                      [WB, xx, xx, BB, WP, xx, BP, xx],
                                      [xx, xx, xx, BP, xx, xx, xx, xx],
                                      [BP, BP, xx, xx, BP, BP, xx, BP],
                                      [BR, BN, BB, BQ, BK, xx, xx, BR]]

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
        self.test_board = Board()
        self.test_board.board_list = [[WR, xx, xx, WQ, WK, WB, xx, WR],
                                      [xx, WP, WP, WP, xx, xx, WP, WP],
                                      [BN, xx, BP, xx, xx, WP, xx, WN],
                                      [WP, xx, WN, xx, xx, xx, xx, xx],
                                      [WB, xx, xx, BR, WP, xx, BP, xx],
                                      [xx, xx, xx, BP, xx, xx, xx, xx],
                                      [BP, BP, xx, xx, BP, BP, xx, BP],
                                      [BR, BN, BB, BQ, BK, BB, xx, xx]]

    def test_black_rook(self):
        self.assertEqual(self.test_board.get_valid_moves(4, 3),
                         {(4, 2), (4, 1), (4, 0), (4, 4), (3, 3), (2, 3), (1, 3)})

    def test_white_rook(self):
        self.assertEqual(self.test_board.get_valid_moves(0, 0), {(1, 0), (2, 0), (0, 1), (0, 2)})


class TestQueenMoves(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()
        self.test_board.board_list = [[WR, xx, xx, xx, WK, WB, xx, WR],
                                      [xx, WP, WP, WP, xx, xx, WP, WP],
                                      [BN, xx, BP, xx, xx, WP, xx, WN],
                                      [WP, xx, WN, WQ, xx, xx, xx, xx],
                                      [WB, xx, xx, xx, WP, xx, BP, xx],
                                      [xx, xx, BQ, BP, xx, xx, xx, xx],
                                      [BP, BP, xx, xx, BP, BP, xx, BP],
                                      [BR, BN, BB, xx, BK, BB, xx, BR]]

    def test_black_queen(self):
        self.assertEqual(self.test_board.get_valid_moves(5, 2),
                         {(5, 1), (5, 0), (6, 2), (6, 3), (4, 3), (3, 4), (2, 5), (4, 2), (3, 2), (4, 1), (3, 0)})

    def test_white_queen(self):
        self.assertEqual(self.test_board.get_valid_moves(3, 3),
                         {(4, 2), (5, 1), (6, 0), (4, 3), (5, 3), (3, 4), (3, 5),
                          (3, 6), (3, 7), (2, 4), (1, 5), (0, 6), (2, 3), (2, 2)})


class TestKingMoves(unittest.TestCase):
    def setUp(self):
        self.test_board = Board()
        self.test_board.board_list = [[WR, xx, xx, xx, WK, WB, xx, WR],
                                      [xx, WP, WP, WP, xx, xx, WP, WP],
                                      [BN, xx, BP, xx, xx, WP, xx, WN],
                                      [WP, WB, WN, WQ, xx, xx, xx, xx],
                                      [xx, xx, xx, xx, WP, xx, BP, xx],
                                      [xx, xx, BQ, BP, xx, xx, xx, xx],
                                      [BP, BP, xx, xx, BP, BP, xx, BP],
                                      [BR, BN, BB, xx, BK, BB, xx, BR]]

    def test_black_king_safe(self):
        self.assertEqual(self.test_board.get_valid_moves(7, 4), {(7, 3), (6, 3)})

    def test_white_king_safe(self):
        self.assertEqual(self.test_board.get_valid_moves(0, 4), {(0, 3), (1, 4), (1, 5)})

    def test_white_king_check(self):
        self.test_board.board_list = [[WR, xx, xx, xx, WK, WB, xx, WR],
                                      [xx, WP, WP, WP, xx, xx, WP, WP],
                                      [BN, xx, BP, xx, xx, WP, xx, WN],
                                      [WP, xx, WN, WQ, BR, xx, xx, xx],
                                      [WB, xx, xx, xx, WP, xx, BP, xx],
                                      [xx, xx, BQ, BP, xx, xx, xx, xx],
                                      [BP, BP, xx, xx, BP, BP, xx, BP],
                                      [BR, BN, BB, xx, BK, BB, xx, xx]]
        self.assertEqual(self.test_board.get_valid_moves(0, 4), {(0, 3), (1, 5)})

    def test_black_king_threat(self):
        self.test_board.board_list = [[WR, xx, xx, xx, WK, WB, xx, WR],
                                      [xx, WP, WP, WP, xx, xx, WP, WP],
                                      [BN, xx, BP, xx, xx, WP, xx, WN],
                                      [WP, xx, WN, WQ, xx, xx, xx, xx],
                                      [xx, xx, xx, xx, WP, WB, BP, xx],
                                      [xx, xx, BQ, BP, xx, xx, xx, xx],
                                      [BP, BP, xx, xx, BP, BP, xx, BP],
                                      [BR, BN, BB, xx, BK, BB, xx, BR]]
        self.assertEqual(self.test_board.get_valid_moves(7, 4), {(7, 3)})


if __name__ == '__main__':
    unittest.main()
