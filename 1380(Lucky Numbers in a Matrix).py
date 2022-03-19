class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])

        min_max = [[[1e5, 1] for _ in range(n)] for _ in range(m)]

        min_row = [0 for _ in range(m)]
        max_col = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if j > 0:
                    if min_max[i][j - 1][0] > matrix[i][j]:
                        min_row[i] = j
                        min_max[i][j][0] = matrix[i][j]
                    else:
                        min_max[i][j][0] = min_max[i][j-1][0]
                else:
                    min_max[i][j][0] = min(min_max[i][j][0], matrix[i][j])

                if i > 0:
                    if min_max[i - 1][j][1] < matrix[i][j]:
                        max_col[j] = i
                        min_max[i][j][1] = matrix[i][j]
                    else:
                        min_max[i][j][1] = min_max[i-1][j][1]
                else:
                    min_max[i][j][1] = max(min_max[i][j][1], matrix[i][j])

        ans = []
        for i, j in enumerate(min_row):
            if max_col[j] == i:
                ans.append(matrix[i][j])

        return ans


matrix = [[3, 7, 8],
          [9, 11, 13],
          [15, 16, 17]]
sol = Solution()
print(sol.luckyNumbers(matrix))
