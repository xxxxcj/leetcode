from queue import Queue


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # q = Queue()
        #
        # q.put((row, column))
        # for i in range(k):
        #     p = Queue()
        #
        #     while not q.empty():
        #         r, c = q.get()
        #         if r + 1 < n and c + 2 < n:
        #             p.put((r + 1, c + 2))
        #         if r + 2 < n and c + 1 < n:
        #             p.put((r + 2, c + 1))
        #         if r + 1 < n and c - 2 >= 0:
        #             p.put((r + 1, c - 2))
        #         if r + 2 < n and c - 1 >= 0:
        #             p.put((r + 2, c - 1))
        #         if r - 1 >= 0 and c + 2 < n:
        #             p.put((r - 1, c + 2))
        #         if r - 2 >= 0 and c + 1 < n:
        #             p.put((r - 2, c + 1))
        #         if r - 1 >= 0 and c - 2 >= 0:
        #             p.put((r - 1, c - 2))
        #         if r - 2 >= 0 and c - 1 >= 0:
        #             p.put((r - 2, c - 1))
        #
        #     q = p
        #
        # return q.qsize() / 8 ** k

        probability_matrix = [[((r + 1 < n and c + 2 < n) +
                                (r + 2 < n and c + 1 < n) +
                                (r + 1 < n and c - 2 >= 0) +
                                (r + 2 < n and c - 1 >= 0) +
                                (r - 1 >= 0 and c + 2 < n) +
                                (r - 2 >= 0 and c + 1 < n) +
                                (r - 1 >= 0 and c - 2 >= 0) +
                                (r - 2 >= 0 and c - 1 >= 0)) / 8 for c in range(n)] for r in range(n)]

        for i in range(1, k):
            m = [[0.0 for _ in range(n)] for _ in range(n)]

            for r in range(len(m)):
                for c in range(len(m[0])):
                    p = 0
                    if r + 1 < n and c + 2 < n:
                        p += probability_matrix[r + 1][c + 2]
                    if r + 2 < n and c + 1 < n:
                        p += probability_matrix[r + 2][c + 1]
                    if r + 1 < n and c - 2 >= 0:
                        p += probability_matrix[r + 1][c - 2]
                    if r + 2 < n and c - 1 >= 0:
                        p += probability_matrix[r + 2][c - 1]
                    if r - 1 >= 0 and c + 2 < n:
                        p += probability_matrix[r - 1][c + 2]
                    if r - 2 >= 0 and c + 1 < n:
                        p += probability_matrix[r - 2][c + 1]
                    if r - 1 >= 0 and c - 2 >= 0:
                        p += probability_matrix[r - 1][c - 2]
                    if r - 2 >= 0 and c - 1 >= 0:
                        p += probability_matrix[r - 2][c - 1]

                    m[r][c] = p/8

            probability_matrix = m

        if k == 0:
            return row < n and column < n

        return probability_matrix[row][column]

n = 8
k = 30
row = 4
column = 6
print(Solution().knightProbability(n, k, row, column))
