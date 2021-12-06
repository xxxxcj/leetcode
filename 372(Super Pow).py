class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        # def binary(b: list):
        #     carry = 0
        #     for i in range(len(b)):
        #         c = b[i] % 2
        #         b[i] = (b[i] + carry * 10) // 2
        #         carry = c
        #
        #     if b[0] == 0:
        #         b.remove(0)
        #
        # a %= 1337
        # c = 1
        # while len(b) > 1 or b[-1] >= 2:
        #     if not b[-1] % 2:
        #         a = (a * a) % 1337
        #     else:
        #         c = (c * a) % 1337
        #         a = (a * a) % 1337
        #     binary(b)
        #
        # return (a * c) % 1337

        a %= 1337
        c = 1
        while len(b) > 1:
            c = (c * pow(a, b[-1], 1337)) % 1337
            a = pow(a, 10, 1337)
            b.pop(-1)

        return (c * pow(a, b[0])) % 1337


sol = Solution()
print(sol.superPow(2, [3]))
