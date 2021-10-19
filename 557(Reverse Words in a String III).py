class Solution:
    def reverseWords(self, s: str) -> str:
        p1 = 0
        n = len(s)
        new_s = ""
        for p2 in range(n):
            if s[p2] == " ":
                for i in range(p2-1, p1-1, -1):
                    new_s += s[i]
                new_s += " "
                p1 = p2 + 1
        for i in range(len(s)-1, p1-1, -1):
            new_s += s[i]
        return new_s