# get all the squares on a board a piece of that type at that location could move to, discounting other pieces on board
WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'
BLACK_PIECES = frozenset([BK, BQ, BR, BB, BN, BP])
WHITE_PIECES = frozenset([WK, WQ, WR, WB, WN, WP])


def white_pawn_move(location, board):
    # TODO en passant
    moves_set = set()
    pos = (location[0] + 1, location[1])
    if valid(board, pos, WHITE_PIECES)[0] and (not valid(board, pos, WHITE_PIECES)[1]):
        moves_set.add(pos)
        pos = (location[0] + 2, location[1])
        # initial move of 2 squares
        if (location[0] == 1) and valid(board, pos, WHITE_PIECES)[0] and not valid(board, pos, WHITE_PIECES)[1]:
            moves_set.add(pos)
    # taking
    for d in (1, -1):
        pos = (location[0] + 1, location[1] + d)
        if valid(board, pos, WHITE_PIECES)[0] and (valid(board, pos, WHITE_PIECES)[1] in BLACK_PIECES):
            moves_set.add(pos)
    return moves_set


def black_pawn_move(location, board):
    # TODO en passant
    moves_set = set()
    pos = (location[0] - 1, location[1])
    if valid(board, pos, BLACK_PIECES)[0] and (not valid(board, pos, BLACK_PIECES)[1]):
        moves_set.add(pos)
        pos = (location[0] - 2, location[1])
        # initial move of 2 squares
        if (location[0] == 6) and valid(board, pos, BLACK_PIECES)[0] and not valid(board, pos, BLACK_PIECES)[1]:
            moves_set.add(pos)
    # taking
    for d in (1, -1):
        pos = (location[0] - 1, location[1] + d)
        if valid(board, pos, BLACK_PIECES)[0] and (valid(board, pos, BLACK_PIECES)[1] in WHITE_PIECES):
            moves_set.add(pos)
    return moves_set


def knight_move(location, board):
    moves_set = set()
    own_pieces = get_own_pieces(location, board)
    for i in ((1, 2), (2, 1)):
        for j in [(x * i[0], y * i[1]) for x in [1, -1] for y in [1, -1]]:
            pos = add_tuples(j, location)
            if valid(board, pos, own_pieces)[0]:
                moves_set.add(pos)
    return moves_set


def rook_move(location, board):
    # TODO castling
    return move_all_directions(location, board, [(1, 0), (-1, 0), (0, 1), (0, -1)])


def bishop_move(location, board):
    return move_all_directions(location, board, [(x, y) for x in [1, -1] for y in [1, -1]])


def queen_move(location, board):
    return bishop_move(location, board).union(rook_move(location, board))


def king_move(location, board):
    # TODO check
    # TODO castling
    return move_all_directions(location, board, [(x, y) for x in [1, -1, 0] for y in [1, -1, 0]])


def move_all_directions(location, board, dirs):
    moves_set = set()
    for d in dirs:
        allowed = True
        pos = add_tuples(d, location)
        while allowed:
            check = valid(board, pos, get_own_pieces(location, board))
            if check[0]:
                moves_set.add(pos)
                if check[1]:
                    allowed = False
            else:
                allowed = False
            pos = add_tuples(d, pos)
    return moves_set


def get_own_pieces(location, board):
    if board[location[0]][location[1]] in WHITE_PIECES:
        return WHITE_PIECES
    else:
        return BLACK_PIECES


def valid(board, pos, bad_pieces):
    if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
        if (board[pos[0]][pos[1]] is None) or (board[pos[0]][pos[1]] not in bad_pieces):
            return True, board[pos[0]][pos[1]]
    return False, None


def add_tuples(a, b):
    return tuple([sum(x) for x in zip(a, b)])

