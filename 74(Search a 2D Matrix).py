class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = [0, 0]
        right = [m - 1, n - 1]

        def get_mid(left, right):
            array_left = left[0] * n + left[1]
            array_right = right[0] * n + right[1]
            array_mid = (array_left + array_right) // 2
            return [array_mid // n, array_mid % n]

        mid = get_mid(left, right)
        while mid != left and mid != right:
            if target == matrix[mid[0]][mid[1]]:
                return True
            if target > matrix[mid[0]][mid[1]]:
                left = mid
            else:
                right = mid
            mid = get_mid(left, right)

        if target == matrix[left[0]][left[1]] or target == matrix[right[0]][right[1]]:
            return True

        return False


matrix = [[1]]
target = 1
print(Solution().searchMatrix(matrix, target))
