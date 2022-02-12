class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        results = []

        def backtrack(i, j, val):
            visited[i][j] = True
            val += grid[i][j]
            can_visit_next_grid = False
            if i - 1 >= 0 and visited[i - 1][j] == False and grid[i - 1][j] > 0:
                can_visit_next_grid = True
                backtrack(i - 1, j, val)
            if i + 1 < m and visited[i + 1][j] == False and grid[i + 1][j] > 0:
                can_visit_next_grid = True
                backtrack(i + 1, j, val)
            if j - 1 >= 0 and visited[i][j - 1] == False and grid[i][j - 1] > 0:
                can_visit_next_grid = True
                backtrack(i, j - 1, val)
            if j + 1 < n and visited[i][j + 1] == False and grid[i][j + 1] > 0:
                can_visit_next_grid = True
                backtrack(i, j + 1, val)

            visited[i][j] = False

            if not can_visit_next_grid:
                results.append(val)

        for i in range(m):
            for j in range(n):
                backtrack(i, j, 0)

        return max(results)

grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
sol = Solution()
print(sol.getMaximumGold(grid))
