class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        flag = True
        while flag:
            flag = False
            if not n % 2:
                n /= 2
                flag = True
            if not n % 3:
                n /= 3
                flag = True
            if not n % 5:
                n /= 5
                flag = True

        return n == 1