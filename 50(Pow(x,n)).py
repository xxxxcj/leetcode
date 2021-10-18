class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n == 1:
            return x

        if n > 0:
            y = self.myPow(x, n // 2)
            if n % 2 == 0:
                return y*y
            else:
                return y*y*x
        if n < 0:
            n = -n
            y = self.myPow(x, n // 2)
            if n % 2 == 0:
                return 1/(y*y)
            else:
                return 1/(y*y*x)


x = 2.0
n = -2

print(Solution().myPow(x,n))
