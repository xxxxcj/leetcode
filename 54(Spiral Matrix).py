class Solution:
    def spiralOrder(self, matrix: list) -> list:
        ans = []

        def add_a_line_to_ans(start: tuple, end: tuple):
            if start[0] == end[0]:
                if start[1] < end[1]:
                    for i in matrix[start[0]][start[1]: end[1] + 1]:
                        ans.append(i)
                    return True
                else:
                    for i in range(start[1], end[1] - 1, -1):
                        ans.append(matrix[start[0]][i])
                    return True
            elif start[1] == end[1]:
                if start[0] < end[0]:
                    for i in range(start[0], end[0] + 1):
                        ans.append(matrix[i][start[1]])
                    return True
                else:
                    for i in range(start[0], end[0] - 1, -1):
                        ans.append(matrix[i][start[1]])
                    return True
            return False

        n0, m0 = 0, 0
        n1 = len(matrix) - 1
        if n1 < 0:
            return ans
        m1 = len(matrix[0]) - 1
        while n1 > n0 and m1 > m0:
            add_a_line_to_ans((n0, m0), (n0, m1))
            # print(ans)
            add_a_line_to_ans((n0 + 1, m1), (n1, m1))
            # print(ans)
            add_a_line_to_ans((n1, m1 - 1), (n1, m0))
            # print(ans)
            if n1 - 1 >= n0 + 1:
                add_a_line_to_ans((n1 - 1, m0), (n0 + 1, m0))
            # print(ans)
            n0 += 1
            m0 += 1
            n1 -= 1
            m1 -= 1

        # print(n0, n1, m0, m1)
        if (n0 == n1 and m0 <= m1) or (m0 == m1 and n0 <= n1):
            add_a_line_to_ans((n0, m0), (n1, m1))
        return ans


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]


print(Solution().spiralOrder(matrix))
