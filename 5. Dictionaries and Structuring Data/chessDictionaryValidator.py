def invalid_board(chessBoard):
    count = {}
    for pos, piece in theBoard.items():
        pieces = ['king', 'queen', 'rook', 'bishop', 'knight', 'pawn']
        name = []
        if (int(pos[0]) > 8 or int(pos[0]) < 0 or ord(pos[1]) > 104 or ord(pos[1]) < 97):
            print('incorrect position ' + pos)
            return False
        if (piece[0] != 'b' and piece[0] != 'w'):
            print('incorrect piece value ' + piece)
            return False
        for i in range(len(piece)-1):
            name.append(piece[i+1])
        if not((''.join(name)).lower() in pieces):
            print('incorrect piece value ' + piece)
            return False
        count.setdefault(piece, 0)
        count[piece] = count[piece] + 1
    for piece, value in count.items():
        if (piece == 'bking' or piece == 'wking' or piece == 'wqueen' or piece == 'bqueen'):
            if (value > 1):
                print('too many ' + piece)
                return False
        if (piece == 'brook' or piece == 'wrook' or piece == 'wbishop' or piece == 'bbishop' or piece == 'wknight' or piece == 'bknight'):
            if (value > 2):
                print('too many ' + piece)
                return False
        else:
            if value > 8:
                print('too many ' + piece)
                return False
    print(count)
    return True

theBoard = {'1a': 'bking', '1b': 'bpawn', '6c': 'bpawn', '2b': 'bbishop', '5h': 'bqueen', '3h': 'wking', '1c': 'bbishop','4b': 'bpawn','4a': 'bpawn','4d': 'bpawn','4e': 'bpawn','4f': 'bpawn','4h': 'bpawn','4g': 'bpawn'}
correctBoard = invalid_board(theBoard)
print (correctBoard)
