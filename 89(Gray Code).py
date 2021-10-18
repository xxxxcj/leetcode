class Solution:
    def grayCode(self, n: int) -> list:
        ret = [0b0, 0b1]
        for i in range(1, n):
            tmp = []
            for j in range(2**i - 1, -1, -1):
                tmp.append(ret[j] + 2**i)
            ret += tmp
        return ret


n = 2
print(Solution().grayCode(n))