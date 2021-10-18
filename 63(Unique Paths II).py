class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            if not obstacleGrid[0][i]:
                dp[0][i] = 1
            else:
                break

        for j in range(m):
            if not obstacleGrid[j][0]:
                dp[j][0] = 1
            else:
                break

        for i in range(1, n):
            for j in range(1, m):
                if not obstacleGrid[j][i]:
                    dp[j][i] = dp[j][i-1] + dp[j-1][i]

        return dp[m-1][n-1]


obstacleGrid = [[0,1],[0,0]]
print(Solution().uniquePathsWithObstacles(obstacleGrid))