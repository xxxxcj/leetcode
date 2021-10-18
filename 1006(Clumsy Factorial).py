class Solution:
    def clumsy(self, N: int) -> int:
        if N <= 4:
            ret = N
            for i in range(1, N):
                if i == 1:
                    ret *= N - i
                elif i == 2:
                    ret //= N - i
                else:
                    ret += N - i
            return ret

        ret = N * (N-1) // (N-2) + N-3
        tmp = 0
        for i in range(4, N):
            if i % 4 == 0:
                ret -= tmp
                tmp = N - i
            elif i % 4 == 1:
                tmp *= N - i
            elif i % 4 == 2:
                tmp //= N - i
            else:
                tmp -= N - i
        return ret - tmp