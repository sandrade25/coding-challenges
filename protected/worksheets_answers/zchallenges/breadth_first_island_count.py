"""
https://www.techiedelight.com/count-the-number-of-islands/

Count number of islands
Given a binary matrix (2d array) where 0 represents water and 1 represents land, and connected ones form an island, count the total islands.

eg:
mat = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
    ]

^ answer: number of islands == 5
"""


from collections import deque


allowed_moves = [(-1,0),(-1,-1),(-1,1),(0,-1),(0,1),(1,-1),(1,0), (1,1)]

def bfs(mat, processed, i, j):
    processed[i][j] = True

    queue = deque([(i,j)])
    while queue:
        cell = queue.popleft()
        for x, y in allowed_moves:
            row = cell[0] + x
            col = cell[1] + y
            
            if row < 0 or row >= len(processed):
                continue

            if col < 0 or col >= len(processed[0]):
                continue

            if mat[row][col] != 1:
                continue

            if processed[row][col]:
                continue

            processed[row][col] = True
            queue.append((row, col))

def breadth_first_island_count(mat):
    if not mat or not len(mat):
        return 0

    (m, n) = (len(mat), len(mat[0]))
    processed = [[False for i in range(n)] for j in range(m)]

    islands = 0
    for i in range(m):
        for j in range(n):
            if not processed[i][j] and mat[i][j] == 1:
                bfs(mat, processed, i, j)
                islands += 1
    return islands


