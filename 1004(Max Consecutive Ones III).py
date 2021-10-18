class Solution:
    def longestOnes(self, A: list, K: int) -> int:
        zero_pos = []
        for idx, item in enumerate(A):
            if item == 0:
                zero_pos.append(idx)

        if len(zero_pos) <= K:
            return len(A)

        max_len = zero_pos[K] - 1

        for i in range(len(zero_pos) - K - 1):
            if zero_pos[i + K + 1] - zero_pos[i] - 1 > max_len:
                max_len = zero_pos[i + K + 1] - zero_pos[i] - 1

        if len(A) - zero_pos[len(zero_pos) - K - 1] > max_len:
            max_len = len(A) - zero_pos[len(zero_pos) - K - 1] - 1

        return max_len


A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K = 3
print(Solution().longestOnes(A, K))
