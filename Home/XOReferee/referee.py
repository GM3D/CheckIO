def get_rows(b):
    return [[b[i][j] for j in range(3)] for i in range(3)]

def get_cols(b):
    return [[b[i][j] for i in range(3)] for j in range(3)]

def get_diagonals(b):
    return [[b[0][0], b[1][1], b[2][2]], [b[0][2], b[1][1], b[2][0]]]

def same_mark(l):
    if (l[0] == 'X' or l[0] == 'O'):
        return (l[0] == l[1] and l[1] == l[2])
    else:
        return False


def checkio(board):
    for row in get_rows(board):
        if same_mark(row):
            return row[0]
    for col in get_cols(board):
        if same_mark(col):
            return col[0]
    for diag in get_diagonals(board):
        if same_mark(diag):
            return diag[0]
    return 'D'

if __name__ == '__main__':
    assert checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X", "Xs wins"
    checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"
