#https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs

"""
Consider a matrix where each cell contains either a 0 or a 1 and any cell containing a 1 is called a filled cell. 
Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. 

If one or more filled cells are also connected, they form a region. 
Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.


Given an m x n matrix, find and print the number of cells in the largest region in the matrix.

"""


"""

[
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1], 
    [0, 1, 1, 1, 0], 
    [0, 0, 0, 0, 1], 
    [1, 1, 1, 0, 0]
]
"""



allowed_moves = [(-1,0), (-1,-1), (-1,1), (0,-1), (0, 1), (1, -1), (1, 0), (1,1)]

def dfs(grid, m, n, v, rows, cols):

    v.append((m, n))
    for move in allowed_moves:
        row = move[0] + m
        col = move[1] + n
        if row < rows and row >= 0 and col < cols and col >= 0 and grid[row][col] == 1 and (row, col) not in v:
            dfs(grid, row, col, v, rows, cols)

    return v

    
    

def dfs_connected_cell_in_grid(grid):
    
    
    rows = len(grid)
    cols = len(grid[0])
    largest_cell_count = 0
    v = set()

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in v and grid[i][j] == 1:
                visited = dfs(grid, i, j, [], rows, cols)
                cell_count = len(visited)
                v = v.union(visited)
                if cell_count > largest_cell_count:
                    largest_cell_count = cell_count
            

    return largest_cell_count
