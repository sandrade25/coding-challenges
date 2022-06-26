"""

given a board as a 2d array, 
find which words in a given list are in the board
by connecting letters horizontally or vertically. 
and without repeating the same cell twice

return a list of boolean values
representing if each word in words can be traced in the board
or not.
"""
moves = [ (0,-1), (-1,0), (0,1), (1,0)]

def dfs(board, word, v, rows, cols, row, col):
    if len(word) <= 1:
        return True

    v[(row, col)] = True
    next = word[1]

    possible_moves = [(row  + nrow, col + ncol) for nrow, ncol in moves]

    for move in possible_moves:
        nrow, ncol = move
        if nrow < 0 or nrow >= rows:
            continue
        if ncol < 0 or ncol >= cols:
            continue
        if v[(nrow, ncol)]:
                continue

        if next == board[nrow][ncol]:
            visited = v.copy()
            if dfs(board, word[1:], visited, rows, cols, nrow, ncol):
                return True

    return False




def dfs_word_in_board(board, words):
    bools = []
    rows = len(board)
    cols = len(board[0])

    v ={(i,j):False for j in range(cols) for i in range(rows)}

    for word in words:
        found = False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited = v.copy()
                    if dfs(board, word, visited, rows, cols, i,j):
                        found = True
                        break
            if found:
                break
            
        bools.append(found)
    return bools