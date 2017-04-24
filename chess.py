WK, WQ, WR, WB, WN, WP = '♔', '♕', '♖', '♗', '♘', '♙'
BK, BQ, BR, BB, BN, BP = '♚', '♛', '♜', '♝', '♞', '♟'


def render_board(pieces_array=None):
    # draw board as a string, given array of pieces
    if not pieces_array:
        return f'{BR} {BN} {BB} {BQ} {BK} {BB} {BN} {BR}\n' + \
               f'{BP} ' * 7 + f'{BP}\n' + \
               '_ _ _ _ _ _ _ _\n' * 4 +\
               f'{WP} ' * 7 + f'{WP}\n' +\
               f'{WR} {WN} {WB} {WQ} {WK} {WB} {WN} {WR}\n'

    elif len(pieces_array) != 8:
        return '_ _ _ _ _ _ _ _\n' * 8
    else:
        pass


def update_board():
    print(render_board())

if __name__ == '__main__':
    update_board()