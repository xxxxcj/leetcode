class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        def gcd(a: int, b: int):
            if b == 0:
                return a
            return gcd(b, a % b)

        fraction_hashmap = {}
        for i in range(1, n + 1):
            for j in range(1, i):
                m, n = i, j
                r = gcd(m, n)
                while r != 1:
                    m /= r
                    n /= r
                    r = gcd(m, n)
                s = str(int(n)) + '/' + str(int(m))
                if s not in fraction_hashmap:
                    fraction_hashmap[s] = 1

        return list(fraction_hashmap.keys())


sol = Solution()
print(sol.simplifiedFractions(100))
