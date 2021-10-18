class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        M = [[1 for _ in range(m)] for _ in range(n)]
        for y in range(1, n):
            for x in range(1, m):
                M[y][x] = M[y-1][x] + M[y][x-1]
        return M[n-1][m-1]


print(Solution().uniquePaths(7, 3))
