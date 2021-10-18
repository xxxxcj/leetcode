import math

class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        ans = 0
        mod = 10 if x >= 0 else -10
        while x != 0:
            ans = ans * 10 + x % mod
            x = math.trunc(x / 10)
        return ans if MIN <= ans <= MAX else 0

x = -1
print(Solution().reverse(x))
