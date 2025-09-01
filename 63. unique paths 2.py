# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 

# Example 1:


# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# Example 2:


# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
 

# Constraints:

# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] is 0 or 1.

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If start or end is an obstacle, no path exists
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            curRow = [0] * n
            for c in range(n - 1, -1, -1):

                if obstacleGrid[r][c] == 1:  # obstacle => no path
                    curRow[c] = 0
                elif r == m - 1 and c == n - 1:  
                    curRow[c] = 1  # destination
                else:
                    right = curRow[c + 1] if c + 1 < n else 0
                    down = prevRow[c] if r + 1 < m else 0
                    curRow[c] = right + down
            prevRow = curRow

        return prevRow[0]
