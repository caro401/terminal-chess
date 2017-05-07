# get all the squares on a board a piece of that type at that location could move to, discounting other pieces on board


def white_pawn_move(location):
    # TODO en passant
    moves_set = set()
    if location[0] < 7:
        moves_set.add((location[0] + 1, location[1]))
    if location[0] == 1:
        moves_set.add((location[0] + 2, location[1]))
    return moves_set


def black_pawn_move(location):
    # TODO en passant
    moves_set = set()
    if location[0] > 0:
        moves_set.add((location[0] - 1, location[1]))
    if location[0] == 6:
        moves_set.add((location[0] - 2, location[1]))
    return moves_set


def rook_move(location):
    moves_set = set()
    for k in range(2):
        x = location[k] - 8
        for i in range(16):
            if 0 <= x < 8:
                if k == 0:
                    moves_set.add((x, location[1]))
                else:
                    moves_set.add((location[0], x))
            x += 1
    moves_set.remove(location)
    return moves_set


def bishop_move(location):
    moves_set = set()
    for diag in [-1, 1]:
        x, y = location[0] - 8, location[1] - (8 * diag)
        for i in range(16):
            if (0 <= x < 8) and (0 <= y < 8):
                moves_set.add((x, y))
            x += 1
            y += diag
    moves_set.remove(location)
    return moves_set


def queen_move(location):
    return bishop_move(location).union(rook_move(location))


def king_move(location):
    moves_set = set()
    for j in [(x, y) for x in [1, -1, 0] for y in [1, -1, 0]]:
        pos = tuple([sum(x) for x in zip(j, location)])
        if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
            moves_set.add(pos)
    moves_set.remove(location)
    return moves_set


def knight_move(location):
    moves_set = set()
    for i in ((1, 2), (2, 1)):
        for j in [(x * i[0], y * i[1]) for x in [1, -1] for y in [1, -1]]:
            pos = tuple([sum(x) for x in zip(j, location)])
            if 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
                moves_set.add(pos)
    return moves_set
