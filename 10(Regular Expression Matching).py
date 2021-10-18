class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        i, j = s_len - 1, p_len - 1

        # print(s, p, i, j)
        if i == -1 and j == -1:
            return True
        elif j < 0 and i > -1:
            return False

        if p[j] != "*" and i > -1:
            if p[j] == s[i] or p[j] == '.':
                return self.isMatch(s[:i], p[:j])
            else:
                return False
        elif i > -1:
            if p[j - 1] == s[i]:
                if self.isMatch(s[:i], p):
                    return True
                else:
                    return self.isMatch(s, p[:j - 1])
            elif p[j - 1] == '.':
                if j - 2 < 0:
                    return True
                else:
                    if s[i] != p[j - 2]:
                        if self.isMatch(s[:i], p):
                            return True
                        else:
                            return self.isMatch(s, p[:j - 1])
                    else:
                        if self.isMatch(s[:i], p[:j - 2]):
                            return True
                        else:
                            return self.isMatch(s[:i], p)
            else:
                return self.isMatch(s, p[:j - 1])
        else:
            if p[j] == "*":
                return self.isMatch(s, p[:j - 1])
            else:
                return False


s = "a"
p = "..*"
print(Solution().isMatch(s, p))
