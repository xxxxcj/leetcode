class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            n = 0
            m = num
            while m > 0:
                n += m % 10
                m //= 10
            num = n
        return num