"""

given a board as a 2d array, 
find which words in a given list are in the board
by connecting letters horizontally or vertically. 
and without repeating the same cell twice

return a list of boolean values
representing if each word in words can be traced in the board
or not.
"""
allowed_moves = [(0,-1), (-1, 0), (0,1), (1,0)]


def dfs_partial(board, visited, word, rows, cols, starting_ix):
    # breakpoint()
    if len(word) > 0:
        next_letter = word[0]
        row, col = starting_ix
        possible_next_ix = [
            (nrow + row, ncol + col) for nrow, ncol in allowed_moves
        ]
        
        found = False
        
        while possible_next_ix and not found:
            new_visited = visited.copy()
            next_ix = possible_next_ix.pop(0)
            nrow, ncol = next_ix
            if nrow < 0 or nrow > rows or ncol < 0 or ncol > cols:
                continue

            if next_letter == board[nrow][ncol] and next_ix not in new_visited:
                new_visited.append(next_ix)
                found = dfs_partial(board, new_visited, word[1:], rows, cols, next_ix)
                

        return found
    return True




def dfs_word_in_board(board, words):
    bools = []
    rows = len(board)
    cols = len(board[0])

    for word in words:
        # breakpoint()
        # first get all indicices of the starting ch in the current word

        # while the list of starting points is not empty
        # set an empty dict of indices visited
        # once an indicie if visited, add it to the dict and mark it True
        # for each ch in the current word, check neighboring indicices from sterting indicie list. 
        # if word completed, mark true in bools list. 
        # if word not completed and no neighbor to jump to, check next starting point and start over. 
        # once no more starting indicies are available, and word still hasnt been completed, mark it false in bools
        
        starting_ix = []
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    starting_ix.append((row, col))


        
        found = False
        while starting_ix and not found:
            ind = starting_ix.pop(0)
            visited = [ind]
            found = dfs_partial(board, visited, word[1:], rows-1, cols-1, ind)


        bools.append(found)

    return bools