class Solution:
    def isToeplitzMatrix(self, matrix: list) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        # for i in range(1, m + n - 2):
        #     pos2, pos1 = max(0, m - i - 1), max(0, i - m + 1)
        #     element = matrix[pos1][pos2]
        #     pos1 += 1
        #     pos2 += 1
        #     while pos1 < n and pos2 < m:
        #         if matrix[pos1][pos2] != element:
        #             return False
        #         pos1 += 1
        #         pos2 += 1
        #
        # return True

        for i in range(n - 1):
            for j in range(m - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(Solution().isToeplitzMatrix(matrix))
