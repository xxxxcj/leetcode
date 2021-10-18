import math

class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        def rotate_cycle(i:int):  # i为第几圈，n为奇数最中心的为0, n为偶数最中心的为0
            if n%2 == 1:
                for j in range(len(matrix[n//2 - i][n//2 - i: n//2 + i])):
                    locations = [(n//2 - i, n//2 - i + j), (n//2 - i + j, n//2 + i), (n//2 + i, n//2 + i - j), (n//2 + i - j, n//2 - i)]
                    tmp0 = matrix[locations[0][0]][locations[0][1]]
                    for k in range(4):
                        tmp1 = matrix[locations[(k+1) % 4][0]][locations[(k+1) % 4][1]]
                        matrix[locations[(k + 1) % 4][0]][locations[(k + 1) % 4][1]] = tmp0
                        tmp0 = tmp1
            else:
                for j in range(len(matrix[n//2 - i - 1][n//2 - i - 1: n//2 + i])):
                    locations = [(n//2 - i - 1, n//2 - i - 1 + j), (n//2 - i - 1 + j, n//2 + i), (n//2 + i, n//2 + i - j), (n//2 + i - j, n//2 - i - 1)]
                    tmp0 = matrix[locations[0][0]][locations[0][1]]
                    for k in range(4):
                        tmp1 = matrix[locations[(k+1) % 4][0]][locations[(k+1) % 4][1]]
                        matrix[locations[(k + 1) % 4][0]][locations[(k + 1) % 4][1]] = tmp0
                        tmp0 = tmp1

        for i in range(math.ceil(n/2)):
            rotate_cycle(i)


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Solution().rotate(matrix)
print(matrix)
