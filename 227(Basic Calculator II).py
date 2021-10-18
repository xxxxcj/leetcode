class Solution:
    def calculate(self, s: str) -> int:
        stk = list()
        n = len(s)
        s_list = list()

        i = 0
        num = ''
        while i < n:
            if ord('0') <= ord(s[i]) <= ord('9'):
                num += s[i]
            elif s[i] != ' ':
                s_list.append(int(num))
                num = ''
                s_list.append(s[i])
            i += 1
        s_list.append(int(num))

        i = 0
        while i < len(s_list):
            if s_list[i] != '*' and s_list[i] != '/':
                stk.append(s_list[i])
            elif s_list[i] == '*':
                stk.append(stk.pop()*s_list[i+1])
                i += 1
            else:
                stk.append(stk.pop()//s_list[i+1])
                i += 1
            i += 1

        i = 0
        ret = stk[0]
        while i < len(stk):
            if stk[i] == '+':
                ret += stk[i+1]
                i += 1
            elif stk[i] == '-':
                ret -= stk[i+1]
                i += 1
            i += 1

        return ret


s = "3/2"
print(Solution().calculate(s))