class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for i in range(len(s)):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        else:
            return "".join(sorted(s))


s = "baaca"
k = 3
print(Solution().orderlyQueue(s, k))
