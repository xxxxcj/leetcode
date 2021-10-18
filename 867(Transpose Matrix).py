class Solution:
    def transpose(self, matrix: list) -> list:
        m, n = len(matrix), len(matrix[0])

        result = []
        for i in range(n):
            result.append([])
            for j in range(m):
                result[i].append(matrix[j][i])

        return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().transpose(matrix))