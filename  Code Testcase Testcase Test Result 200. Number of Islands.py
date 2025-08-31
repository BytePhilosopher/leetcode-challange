# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            # base case: stop if out of bounds, already visited, or water
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                (r, c) in visit or grid[r][c] == "0"):
                return

            # mark this cell as visited
            visit.add((r, c))

            # explore neighbors (up, down, left, right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                # if we find land not visited yet, it's a new island
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1

        return islands
