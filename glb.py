from typing import List, NewType, Tuple, Optional

COLS_MAP = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'
BLACK_PIECES = frozenset([BK, BQ, BR, BB, BN, BP])
WHITE_PIECES = frozenset([WK, WQ, WR, WB, WN, WP])

BoardList = NewType('BoardList', List[List[Optional[str]]])
Coordinates = NewType('Coordinates', Tuple[int, int])
