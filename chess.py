WKING, WQUEEN, WROOK, WBISHOP, WKNIGHT, WPAWN = '♔', '♕', '♖', '♗', '♘', '♙'
BKING, BQUEEN, BROOK, BBISHOP, BKNIGHT, BPAWN = '♚', '♛', '♜', '♝', '♞', '♟'


def render_board(pieces_array=None):
    if not pieces_array:
        return '_ _ _ _ _ _ _ _\n' * 8
    else:
        pass


def update_board():
    print(render_board())

if __name__ == '__main__':
    update_board()