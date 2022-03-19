class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = ""
        is_negative = False
        if num < 0:
            is_negative = True
            num = -num

        while num > 0:
            ans = str(num % 7) + ans
            num //= 7

        if is_negative:
            ans = '-' + ans

        if ans == '':
            ans += '0'

        return ans


sol = Solution()
print(sol.convertToBase7(0))