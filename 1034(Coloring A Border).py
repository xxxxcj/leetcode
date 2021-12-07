class Solution:
    def colorBorder(self, grid: list, row: int, col: int, color: int) -> list:
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        grid_new = [[grid[j][i] for i in range(n)] for j in range(m)]

        def find_connection(row: int, col: int, c: int):
            visited[row][col] = 1
            count = 0
            if row + 1 < m and grid[row + 1][col] == c:
                count += 1
                if not visited[row + 1][col]:
                    visited[row + 1][col] = 1
                    find_connection(row + 1, col, c)
            if col + 1 < n and grid[row][col + 1] == c:
                count += 1
                if not visited[row][col + 1]:
                    visited[row][col + 1] = 1
                    find_connection(row, col + 1, c)
            if row - 1 >= 0 and grid[row - 1][col] == c:
                count += 1
                if not visited[row - 1][col]:
                    visited[row - 1][col] = 1
                    find_connection(row - 1, col, c)
            if col - 1 >= 0 and grid[row][col - 1] == c:
                count += 1
                if not visited[row][col - 1]:
                    visited[row][col - 1] = 1
                    find_connection(row, col - 1, c)

            if count != 4:
                grid_new[row][col] = color

        find_connection(row, col, grid[row][col])
        return grid_new


grid = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]
row = 1
col = 1
color = 2
sol = Solution()
print(sol.colorBorder(grid, row, col, color))
