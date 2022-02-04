class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stk = []

        ans = ""
        for idx, c in enumerate(word):
            if c == ch:
                stk.append(c)
                while len(stk) != 0:
                    ans += stk.pop()
                ans += word[idx+1:]
                break
            else:
                stk.append(c)

        if len(stk) == len(word):
            return word
        return ans


word = "abcd"
ch = 'z'
sol = Solution()
print(sol.reversePrefix(word, ch))
