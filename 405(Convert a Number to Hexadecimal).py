class Solution:
    def toHex(self, num: int) -> str:
        hex_dict = [str(i) for i in range(10)]
        hex_dict += ['a', 'b', 'c', 'd', 'e', 'f']

        a = 15
        ans = ""
        for i in range(8):
            b = a & num
            num //= 16
            ans = hex_dict[b] + ans
            if num == 0:
                break

        return ans


sol = Solution()
print(sol.toHex(0))
