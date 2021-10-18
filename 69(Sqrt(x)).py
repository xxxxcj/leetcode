class Solution:
    def mySqrt(self, x: int) -> int:
        # brute force
        # for i in range(x):
        #     if i*i > x:
        #         return i-1
        # return 0 if x == 0 else 1

        if x < 4:
            return 0 if x == 0 else 1
        left, right = 0, x
        while right - left != 1:
            mid = (left + right) // 2
            if mid*mid > x:
                right = mid
            elif mid*mid < x:
                left = mid
            else:
                return mid

        return left


for i in range(100000):
    print(i, Solution().mySqrt(i))