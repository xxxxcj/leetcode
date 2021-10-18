class Solution:
    def convert(self, s: str, numRows: int) -> str:
        gap = 2*numRows - 2 if 2*numRows - 2 > 0 else 1
        ans = ""
        tmp = 0
        centre = []
        s_len = len(s)
        for i in range(numRows):
            if 0 < i < numRows - 1:
                for j in centre:
                    if 0 < j - i < s_len:
                        ans += s[j - i]
                    if j + i < s_len:
                        ans += s[j + i]
            elif i == 0:
                while tmp < len(s):
                    ans += s[tmp]
                    centre.append(tmp)
                    tmp += gap
                centre.append(tmp)
            else:
                for j in centre:
                    if j + i < s_len:
                        ans += s[j + i]
        return ans


s = "PAYPALISHIRING"
print(Solution().convert(s, 3))
