class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row = [False for _ in range(n)]
        col = [False for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    row[j] = True
                    col[i] = True

        for i in range(m):
            if col[i]:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(n):
            if row[j]:
                for i in range(m):
                    matrix[i][j] = 0