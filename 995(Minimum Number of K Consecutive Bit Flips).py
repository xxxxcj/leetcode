class Solution:
    def minKBitFlips(self, A: list, K: int) -> int:
        # result = 0
        # n = len(A)
        # for i in range(n - K + 1):
        #     if not A[i]:
        #         result += 1
        #         for j in range(i, i+K):
        #             A[j] = (A[j] + 1) % 2
        #
        # i = 0
        # while i < K:
        #     if not A[n - i - 1]:
        #         return -1
        #     i += 1
        # return result

        result = 0
        n = len(A)

        if K == 1:
            return n - sum(A)

        diff = [0 for _ in range(n)]
        times = 0
        for i in range(n - K + 1):
            if not (A[i] + times + diff[i]) % 2:
                result += 1
                diff[i] += 1
                if i + K < n:
                    diff[i + K] -= 1
            times += diff[i]

        print(diff)
        times = 0
        for i in range(n):
            times += diff[i]
            if not (A[i] + times) % 2:
                return -1

        return result


A = [0,0,0,1,0,1,1,0]
K = 3
print(Solution().minKBitFlips(A, K))
