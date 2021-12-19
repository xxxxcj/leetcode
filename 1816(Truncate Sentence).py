class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for idx, ch in enumerate(s):
            if ch == ' ':
                k -= 1
                if k == 0:
                    return s[:idx-1]
        return s