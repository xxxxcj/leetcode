class NumMatrix:

    def __init__(self, matrix: list):
        if len(matrix) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])

        self.sum_of_pos = [[0 for _ in range(n + 1)]]

        for j in range(1, m + 1):
            self.sum_of_pos.append([0])
            for i in range(1, n + 1):
                self.sum_of_pos[j].append(
                    self.sum_of_pos[j][i - 1] + self.sum_of_pos[j - 1][i] - self.sum_of_pos[j - 1][i - 1]
                    + matrix[j - 1][i - 1])

        for i in self.sum_of_pos:
            print(i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum_of_pos[row2 + 1][col2 + 1] + self.sum_of_pos[row1][col1] \
               - self.sum_of_pos[row1][col2 + 1] - self.sum_of_pos[row2 + 1][col1]


tmp = [
    [
        [[3, 0, 1, 4, 2],
         [5, 6, 3, 2, 1],
         [1, 2, 0, 1, 5],
         [4, 1, 0, 1, 7],
         [1, 0, 3, 0, 5]]
    ],
    [2, 1, 4, 3],
    [1, 1, 2, 2],
    [1, 2, 2, 4]]

# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix(tmp[0][0])
param_1 = obj.sumRegion(1, 1, 2, 2)
print(param_1)
