class Solution:
    def generateMatrix(self, n: int):

        def add_direction(n, m, k):
            n += direction[k%4][0]
            m += direction[k%4][1]
            return n, m

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False for i in range(n)] for i in range(n)]
        matrix = [[0 for i in range(n)] for i in range(n)]
        r, m, k = 0, 0, 0
        for i in range(n*n):
            matrix[r][m] = i+1
            r_tmp, m_tmp = add_direction(r, m, k)
            visited[r][m] = True
            if r_tmp >= n or r_tmp < 0 or m_tmp >= n or m_tmp < 0 or visited[r_tmp][m_tmp]:
                k += 1
                r, m = add_direction(r, m, k)
            else:
                r, m = r_tmp, m_tmp
        return matrix


n = 3
print(Solution().generateMatrix(3))
