class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def binary_search(x1, x2, y1, y2):
            if x1 == x2 - 1:
                for i in range(y1, y2):
                    if matrix[i][x1] == target:
                        return True
                return False
            elif y1 == y2 - 1:
                for i in range(x1, x2):
                    if matrix[y1][i] == target:
                        return True
                return False

            x_mid = (x2 + x1) // 2
            y_mid = (y2 + y1) // 2

            if matrix[y_mid][x_mid] == target:
                return True
            elif matrix[y_mid][x_mid] > target:
                return binary_search(x1, x_mid, y1, y_mid) or \
                       binary_search(x_mid, x2, y1, y_mid) or \
                       binary_search(x1, x_mid, y_mid, y2)
            else:
                return binary_search(x_mid, x2, y_mid, y2) or \
                       binary_search(x_mid, x2, y1, y_mid) or \
                       binary_search(x1, x_mid, y_mid, y2)

        return binary_search(0, n, 0, m)


matrix = [[1, 4, 7, 11, 15],
          [2, 5, 8, 12, 19],
          [3, 6, 9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]
sol = Solution()
for target in range(0, 31):
    print(target, sol.searchMatrix(matrix, target))
