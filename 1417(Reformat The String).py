class Solution:
    def reformat(self, s: str) -> str:
        chs = []
        digits = []
        for c in s:
            if ord('0') <= ord(c) <= ord('9'):
                digits.append(c)
            else:
                chs.append(c)

        ans = ""
        if abs(len(chs) - len(digits)) <= 1:
            if len(chs) < len(digits):
                while len(chs) != 0:
                    ans += digits.pop()
                    ans += chs.pop()
                ans += digits.pop()
            else:
                while len(digits) != 0:
                    ans += chs.pop()
                    ans += digits.pop()
                if len(chs) == 1:
                    ans += chs.pop()
        return ans