class Solution:
    def toLowerCase(self, s: str) -> str:
        # return s.lower()

        def char2lower(ch: str):
            return chr(ord(ch) - ord('A') + ord('a'))

        ans = ""
        for ch in s:
            if ord("A") <= ord(ch) <= ord("Z"):
                ans += char2lower(ch)
            else:
                ans += ch

        return ans