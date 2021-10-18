class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n:
            n &= n-1
            ret += 1
        return ret


n = 0b00000000000000000000000000001011
print(Solution().hammingWeight(n))
