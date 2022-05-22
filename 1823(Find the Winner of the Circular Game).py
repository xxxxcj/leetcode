from queue import Queue


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = Queue(n)

        for i in range(n):
            q.put(i + 1)

        gap = 0
        while q.qsize() != 1:
            idx = q.get()
            gap += 1
            if gap == k:
                gap = 0
            else:
                q.put(idx)

        return q.get()


n = 6
k = 5
print(Solution().findTheWinner(n, k))
