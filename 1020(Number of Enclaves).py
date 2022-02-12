class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if ((i == 0 or i == m-1) or (j == 0 or j == n - 1)) and not visited[i][j] and grid[i][j] == 1:
                    dfs(i, j)

        ans = 0
        for i in range(1,m -1):
            for j in range(1, n-1):
                if not visited[i][j]:
                    ans += grid[i][j]

        return ans

grid = [[0, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]]
sol = Solution()
print(sol.numEnclaves(grid))
