from typing import List

class Solution:
    def dfs(self, grid: List[List[str]], row: int, column: int):
        nr = len(grid)
        nc = len(grid[0])

        if row < 0 or column < 0 or \
            row >= nr or column >= nc or \
            grid[row][column] == '0':
            return

        grid[row][column] = '0'
        self.dfs(grid, row-1, column)
        self.dfs(grid, row+1, column)
        self.dfs(grid, row, column-1)
        self.dfs(grid, row, column+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0

        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_islands += 1
                    self.dfs(grid, r, c)
        
        return num_islands


        