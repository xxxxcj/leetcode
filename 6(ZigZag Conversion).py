class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        gap = max(1, 2*numRows - 2)
        for row in range(numRows):
            if row == 0 or row == numRows - 1:
                i = row
                while i < len(s):
                    ans += s[i]
                    i += gap
            else:
                i = row
                while i < len(s):
                    ans += s[i]
                    if i + 2*(numRows - 1 - row) < len(s):
                        ans += s[i + 2*(numRows - 1 - row)]
                    i += gap
        return ans


s = "A"
print(Solution().convert(s, 1))
