class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        def segisValid(s:str):
            s_len = len(s)
            if s_len > 3 or (s_len > 1 and s[0] == '0'):
                return False
            if s_len == 2:
                s = '0' + s
            elif s_len == 1:
                s = '00' + s
            return '000' <= s <= '255'

        def IPisValid(s:str, p1, p2, p3):
            return segisValid(s[:p1 + 1]) and \
                   segisValid(s[p1 + 1: p2 + 1]) and \
                   segisValid(s[p2 + 1: p3 + 1]) and \
                   segisValid(s[p3 + 1:])

        ans = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    p1 = i
                    p2 = p1 + j + 1
                    p3 = p2 + k + 1
                    if p3 >= len(s):
                        break
                    if IPisValid(s, p1, p2, p3):
                        ans.append(s[:p1 + 1] + '.' + s[p1 + 1: p2 + 1] + '.' + s[p2 + 1: p3 + 1] + '.' + s[p3 + 1:])

        return ans


s = "010010"
print(Solution().restoreIpAddresses(s))
