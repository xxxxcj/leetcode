class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        area = 0
        n, m = len(grid), len(grid[0])
        col_max = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                area += min(1, grid[i][j])
                if grid[i][j] > col_max[j]:
                    col_max[j] = grid[i][j]
            area += max(grid[i])
        area += sum(col_max)
        return area
