class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 0
        j = 3
        count = 0
        while i < n:
            count += 1
            i += j
            j += 2
        return count


sol = Solution()
print(sol.bulbSwitch(10000))
