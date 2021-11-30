class Solution:
    def findNthDigit(self, n: int) -> int:
        bits = 0
        while n > bits * 9 * 10 ** (bits - 1):
            n -= bits * 9 * 10 ** (bits - 1)
            bits += 1

        n = int(n) - 1

        num = n // bits + 10 ** (bits - 1)
        b = n % bits
        print(bits, num, b)
        while bits - b - 1 > 0:
            b += 1
            num //= 10
        return num % 10


sol = Solution()
print(sol.findNthDigit(100000))


