class Solution:

    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n: int) -> list:
        self.generate('', 0, 0, n)
        return self.ans

    def generate(self, s, left, right, n):
        if len(s) == 2*n:
            self.ans.append(s)
            return
        if left < n:
            s += '('
            self.generate(s, left+1, right, n)
            s = s[:-1]
        if right < left:
            s += ')'
            self.generate(s, left, right+1, n)


print(Solution().generateParenthesis(5))




