from glb import *
from typing import Set, FrozenSet


class Board:
    def __init__(self) -> None:
        self.board_list: BoardList = [[WR, WN, WB, WQ, WK, WB, WN, WR], [WP] * 8, [None] * 8, [None] * 8,
                                      [None] * 8, [None] * 8, [BP] * 8, [BR, BN, BB, BQ, BK, BB, BN, BR]]
        self.moves_map = {WP: self.pawn_move, BP: self.pawn_move, BR: self.rook_move, WR: self.rook_move,
                          WB: self.bishop_move, BB: self.bishop_move, WQ: self.queen_move, BQ: self.queen_move,
                          WN: self.knight_move, BN: self.knight_move, WK: self.king_move, BK: self.king_move}

    def make_move(self, origin: Coordinates, target: Coordinates) -> None:
        self.board_list[target[0]][target[1]], self.board_list[origin[0]][origin[1]] = \
            self.board_list[origin[0]][origin[1]], None

    def get_valid_moves(self, row: int, col: int) -> Set[Coordinates]:
        return self.moves_map[self.board_list[row][col]]((row, col))

    def pawn_move(self, location: Coordinates) -> Set[Coordinates]:
        moves_set: Set[Coordinates] = set()
        if self.board_list[location[0]][location[1]] in BLACK_PIECES:
            colour, own_pieces, other_pieces, start_row = -1, BLACK_PIECES, WHITE_PIECES, 6
        else:
            colour, own_pieces, other_pieces, start_row = 1, WHITE_PIECES, BLACK_PIECES, 1
        pos: Coordinates = (location[0] + colour, location[1])
        if self.valid(pos, own_pieces)[0] and (not self.valid(pos, own_pieces)[1]):
            moves_set.add(pos)
            pos = (location[0] + (2 * colour), location[1])
            # initial move of 2 squares
            if (location[0] == start_row) and self.valid(pos, own_pieces)[0] and not self.valid(pos, own_pieces)[1]:
                moves_set.add(pos)
        for d in (1, -1):
            pos = (location[0] + colour, location[1] + d)
            if self.valid(pos, own_pieces)[0] and (self.valid(pos, own_pieces)[1] in other_pieces):
                moves_set.add(pos)
        return moves_set

    def knight_move(self, location: Coordinates) -> Set[Coordinates]:
        return self.move_all_directions_limited(location, [(x * i[0], y * i[1]) for x in [1, -1] for y in [1, -1]
                                                           for i in ((1, 2), (2, 1))])

    def rook_move(self, location: Coordinates) -> Set[Coordinates]:
        # TODO castling
        return self.move_all_directions_edge(location, [(1, 0), (-1, 0), (0, 1), (0, -1)])

    def bishop_move(self, location: Coordinates) -> Set[Coordinates]:
        return self.move_all_directions_edge(location, [(x, y) for x in [1, -1] for y in [1, -1]])

    def queen_move(self, location: Coordinates) -> Set[Coordinates]:
        return self.bishop_move(location).union(self.rook_move(location))

    def king_move(self, location: Coordinates) -> Set[Coordinates]:
        # TODO check
        # TODO castling
        return self.move_all_directions_limited(location, [(x, y) for x in [1, -1, 0] for y in [1, -1, 0]])

    def move_all_directions_edge(self, location: Coordinates, dirs: List[tuple]) -> Set[Coordinates]:
        # for rook, bishop, queen - moves can extend to edge of board
        moves_set: Set[Coordinates] = set()
        for d in dirs:
            allowed: bool = True
            pos: Coordinates = self.add_tuples(d, location)
            while allowed:
                check = self.valid(pos, self.get_own_pieces(location))
                if check[0]:
                    moves_set.add(pos)
                    if check[1]:
                        allowed = False
                else:
                    allowed = False
                pos = self.add_tuples(d, pos)
        return moves_set

    def move_all_directions_limited(self, location: Coordinates, dirs: List[tuple]) -> Set[Coordinates]:
        # for knight, king - moves can only take 1 step
        moves_set: Set[Coordinates] = set()
        own_pieces: Set[str] = self.get_own_pieces(location)
        for d in dirs:
            pos: tuple = self.add_tuples(d, location)
            if self.valid(pos, own_pieces)[0]:
                moves_set.add(pos)
        return moves_set

    def get_own_pieces(self, location: Coordinates) -> FrozenSet[str]:
        if self.board_list[location[0]][location[1]] in WHITE_PIECES:
            return WHITE_PIECES
        else:
            return BLACK_PIECES

    def valid(self, pos: Coordinates, bad_pieces: FrozenSet[str]) -> Tuple[bool, Optional[List]]:
        if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
            if (self.board_list[pos[0]][pos[1]] is None) or (self.board_list[pos[0]][pos[1]] not in bad_pieces):
                return True, self.board_list[pos[0]][pos[1]]
        return False, None
    
    @staticmethod
    def add_tuples(a: Tuple[int, int], b: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple([sum(x) for x in zip(a, b)])
