class Solution:
    def isNumber(self, s: str) -> bool:

        s = s.strip(' ')

        if len(s) == 0:
            return False

        def is_int(s):
            if len(s) == 0:
                return False

            if s[0] > '9' or s[0] < '0':
                if s[0] != '+' and s[0] != '-':
                    return False
                else:
                    s = s[1:]

            if len(s) == 0:
                return False

            for i in s:
                if i > '9' or i < '0':
                    return False
            return True

        point = False
        if s[0] > '9' or s[0] < '0':
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            if s[0] == '.':
                point = True
                s = s[1:]

        if len(s) == 0:
            return False

        for i in range(len(s)):
            if s[i] > '9' or s[i] < '0':
                if s[i] == '.':
                    if not point:
                        point = True
                    else:
                        return False
                elif (s[i] == 'e' or s[i] == 'E') and i > 0:
                    return is_int(s[i + 1:])
                else:
                    return False

        return True


s = "-1E-16"
print(Solution().isNumber(s))
