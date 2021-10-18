class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2147483647
        MIN = -2147483648

        if divisor*dividend < 0:
            sign = False
        else:
            sign = True

        divisor = abs(divisor)
        dividend = abs(dividend)

        if divisor <= dividend:
            ans = 1
            a = divisor
            while a + a < dividend:
                ans = ans + ans
                a += a
            ans += self.divide(dividend - a, divisor)
        else:
            ans = 0

        if sign:
            if ans > MAX:
                return MAX
            else:
                return ans
        else:
            if -ans < MIN:
                return MIN
            else:
                return -ans


x = 1
y = 1
print(Solution().divide(x,y))
