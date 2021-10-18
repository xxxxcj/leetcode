class Solution:
    def calculate(self, s: str) -> int:
        stk = list()

        def str_to_num(num):
            ret = 0
            for i in num:
                ret *= 10
                ret += int(i)
            return ret

        num = ''
        for ch in s:
            if ch != ')':
                if ch == '+' or ch == '-':
                    if num != '':
                        stk.append(str_to_num(num))
                        num = ''
                    stk.append(ch)
                elif ch == '(':
                    stk.append(ch)
                elif ch != ' ':
                    num += ch
            else:
                result = 0
                tmp = str_to_num(num)
                num = ''
                while stk[-1] != '(':
                    ch = stk.pop()
                    if ch == '-':
                        tmp = -tmp
                    elif ch == '+':
                        pass
                    else:
                        result += tmp
                        tmp = ch

                stk.pop()
                stk.append(result + tmp)

        if num != '':
            stk.append(str_to_num(num))
        result = 0
        tmp = stk.pop()
        while len(stk) != 0:
            ch = stk.pop()
            if ch == '-':
                tmp = -tmp
            elif ch == '+':
                pass
            else:
                result += tmp
                tmp = ch

        return result + tmp


s = "1+1"
print(Solution().calculate(s))