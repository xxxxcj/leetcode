class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"M":1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        ans = 0
        s_len = len(s)
        i = s_len - 1
        threshold = 0
        while i >= 0:
            tmp = roman_to_int[s[i]]
            if tmp >= threshold:
                ans += tmp
                threshold = tmp
            else:
                ans -= tmp
            i -= 1
        return ans


s = "LVIII"
print(Solution().romanToInt(s))
