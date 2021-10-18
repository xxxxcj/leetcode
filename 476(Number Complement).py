class Solution:
    def findComplement(self, num: int) -> int:
        n = 0
        m = num
        while m != 0:
            n += 1
            m //= 2

        return 2**n - num - 1


sol = Solution()
num = 5
print(sol.findComplement(num))