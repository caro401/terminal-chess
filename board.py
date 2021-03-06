from copy import deepcopy
from glb import *
from typing import Set, FrozenSet

# TODO stop pieces moving such that they leave king in check
# TODO check mate


class Board:
    def __init__(self) -> None:
        self.board_list: BoardList = [[WR, WN, WB, WQ, WK, WB, WN, WR],
                                      [WP] * 8,
                                      [None] * 8,
                                      [None] * 8,
                                      [None] * 8,
                                      [None] * 8,
                                      [BP] * 8,
                                      [BR, BN, BB, BQ, BK, BB, BN, BR]]
        self.moves_map = {WP: self.pawn_move, BP: self.pawn_move,
                          BR: self.rook_move, WR: self.rook_move,
                          WB: self.bishop_move, BB: self.bishop_move,
                          WQ: self.queen_move, BQ: self.queen_move,
                          WN: self.knight_move, BN: self.knight_move,
                          WK: self.king_move, BK: self.king_move}
        self.current_board: BoardList = deepcopy(self.board_list)
        # for hypothetical moves

    def make_move(self, origin: Coordinates,
                  target: Coordinates) -> None:
        self.board_list[target[0]][target[1]],
        self.board_list[origin[0]][origin[1]] = \
            self.board_list[origin[0]][origin[1]], None

    def make_temp_move(self, origin: Coordinates,
                       target: Coordinates) -> BoardList:
        original = self.current_board = deepcopy(self.board_list)
        self.current_board[target[0]][target[1]], \
            self.current_board[origin[0]][origin[1]] = \
            original[origin[0]][origin[1]], None

    def get_valid_moves(self, row: int, col: int) -> Set[Coordinates]:
        self.current_board: BoardList = deepcopy(self.board_list)
        potential_moves: Set[Coordinates] \
            = self.moves_map[self.board_list[row][col]]((row, col))
        opposing_pieces: FrozenSet[str] = self.get_enemy_pieces((row, col))
        opposing_locations: Set[Coordinates] \
            = self.find_pieces(opposing_pieces - set([WK, BK]))
        allowed_moves = set()
        for move in potential_moves:
            self.make_temp_move((row, col), move)
            king_pos: Coordinates = self.find_king(WK if
                                               opposing_pieces == BLACK_PIECES
                                               else BK)
            opposing_moves = set()
            # find all the possible moves for the opposing pieces
            for piece_loc in opposing_locations:
                opposing_moves.update(self.moves_map[
                    self.current_board[piece_loc[0]][piece_loc[1]]](piece_loc))
            if king_pos not in opposing_moves:
                allowed_moves.add(move)
        self.current_board: BoardList = deepcopy(self.board_list)
        return allowed_moves

    def find_king(self, king: str) -> Coordinates:
        return [(ix, iy) for ix, row in enumerate(self.current_board)
                for iy, i in enumerate(row) if i == king][0]

    def find_pieces(self, pieces_set: Set[str]) -> Set[Coordinates]:
        piece_locs = set()
        for i in range(8):
            for j in range(8):
                if self.board_list[j][i] in pieces_set:
                    piece_locs.add((j, i))
        return piece_locs

    def pawn_move(self, location: Coordinates) -> Set[Coordinates]:
        moves_set: Set[Coordinates] = set()
        if self.current_board[location[0]][location[1]] in BLACK_PIECES:
            colour, own_pieces, other_pieces, start_row \
                = -1, BLACK_PIECES, WHITE_PIECES, 6
        else:
            colour, own_pieces, other_pieces, start_row \
                = 1, WHITE_PIECES, BLACK_PIECES, 1
        pos: Coordinates = (location[0] + colour, location[1])
        if self.valid(pos, own_pieces)[0] \
           and (not self.valid(pos, own_pieces)[1]):
            moves_set.add(pos)
            pos = (location[0] + (2 * colour), location[1])
            # initial move of 2 squares
            if (location[0] == start_row) and self.valid(pos, own_pieces)[0] \
                    and not self.valid(pos, own_pieces)[1]:
                moves_set.add(pos)
        for d in (1, -1):
            pos = (location[0] + colour, location[1] + d)
            if self.valid(pos, own_pieces)[0] and (self.valid(pos, own_pieces)[
                    1] in other_pieces):
                moves_set.add(pos)
        return moves_set

    def knight_move(self, location: Coordinates) -> Set[Coordinates]:
        return self.move_all_directions_limited(location,
                                                [(x * i[0], y * i[1])
                                                 for x in [1, -1]
                                                 for y in [1, -1]
                                                 for i in ((1, 2), (2, 1))])

    def rook_move(self, location: Coordinates) -> Set[Coordinates]:
        # TODO castling
        return self.move_all_directions_edge(
            location, [(1, 0), (-1, 0), (0, 1), (0, -1)])

    def bishop_move(self, location: Coordinates) -> Set[Coordinates]:
        return self.move_all_directions_edge(location, [(x, y)
                                                        for x in [1, -1]
                                                        for y in [1, -1]])

    def queen_move(self, location: Coordinates) -> Set[Coordinates]:
        return self.bishop_move(location).union(self.rook_move(location))

    def king_move(self, location: Coordinates) -> Set[Coordinates]:
        # TODO castling
        enemy_pieces: FrozenSet[str] = self.get_enemy_pieces(location)
        potential_moves: Set[Coordinates] = \
            self.move_all_directions_limited(location, [(x, y)
                                                        for x in [1, -1, 0]
                                                        for y in [1, -1, 0]])
        good_moves: Set[Coordinates] = set()
        for move in potential_moves:
            if not self.check_for_check(move, enemy_pieces):
                good_moves.add(move)
        return good_moves

    def move_all_directions_edge(self, location: Coordinates,
                                 dirs: List[tuple]) -> Set[Coordinates]:
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

    def move_all_directions_limited(self, location: Coordinates,
                                    dirs: List[tuple]) -> Set[Coordinates]:
        # for knight, king - moves can only take 1 step
        moves_set: Set[Coordinates] = set()
        own_pieces: Set[str] = self.get_own_pieces(location)
        for d in dirs:
            pos: tuple = self.add_tuples(d, location)
            if self.valid(pos, own_pieces)[0]:
                moves_set.add(pos)
        return moves_set

    def get_own_pieces(self, location: Coordinates) -> FrozenSet[str]:
        return WHITE_PIECES \
            if self.current_board[location[0]][location[1]] in WHITE_PIECES \
            else BLACK_PIECES

    def get_enemy_pieces(self, location: Coordinates) -> FrozenSet[str]:
        return WHITE_PIECES \
            if self.current_board[location[0]][location[1]] in BLACK_PIECES \
            else BLACK_PIECES

    def valid(self, pos: Coordinates,
              bad_pieces: FrozenSet[str]) -> Tuple[bool, Optional[List]]:
        if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
            if (self.current_board[pos[0]][pos[1]] is None)\
               or (self.current_board[pos[0]][pos[1]] not in bad_pieces):
                return True, self.current_board[pos[0]][pos[1]]
        return False, None

    def check_for_check(self, king_pos: Coordinates,
                        bad_pieces: FrozenSet[str]) -> bool:
        next_moves: Set[Coordinates] = set()
        for i in range(8):
            for j in range(8):
                current_sq = self.current_board[i][j]
                if current_sq in (BK, WK):
                    continue
                if self.current_board[i][j] in bad_pieces:
                    next_moves = next_moves.union(self.get_valid_moves(i, j))
                    if king_pos in next_moves:
                        return True
        return False

    @staticmethod
    def add_tuples(a: Tuple[int, int], b: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple([sum(x) for x in zip(a, b)])
