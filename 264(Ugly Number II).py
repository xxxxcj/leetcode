class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0, 1]
        p2, p3, p5 = 1, 1, 1
        i = 1
        while i < n:
            num1 = dp[p2]*2
            num2 = dp[p3]*3
            num3 = dp[p5]*5
            if dp[-1] == num1:
                p2 += 1
            elif dp[-1] == num2:
                p3 += 1
            elif dp[-1] == num3:
                p5 += 1
            else:
                dp.append(min(min(num1, num2), num3))
                i += 1

        return dp[-1]


print(Solution().nthUglyNumber(10))