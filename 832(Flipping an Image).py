class Solution:
    def flipAndInvertImage(self, A: list) -> list:
        m = len(A)
        n = len(A[0])

        result = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = (A[i][n-j - 1] + 1) % 2

        return result


A = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(A))