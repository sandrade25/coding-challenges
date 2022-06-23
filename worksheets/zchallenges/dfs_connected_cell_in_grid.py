#https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=graphs

"""
Consider a matrix where each cell contains either a 0 or a 1 and any cell containing a 1 is called a filled cell. 
Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. 

If one or more filled cells are also connected, they form a region. 
Note that each cell in a region is connected to at least one other cell in the region but is not necessarily directly connected to all the other cells in the region.


Given an m x n matrix, find and print the number of cells in the largest region in the matrix.

"""

def dfs_connected_cell_in_grid(grid):
    return