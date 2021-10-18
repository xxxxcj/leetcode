class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # t = preorder.split(',')
        # n = len(t)
        # p = [0]
        #
        # def is_btree():
        #     if p[0] >= n:
        #         return False
        #     if t[p[0]] == '#':
        #         p[0] += 1
        #         return True
        #     p[0] += 1
        #     return is_btree() and is_btree()
        #
        # return is_btree() and p[0] == n

        t = preorder.split(',')
        stk = [['#', False]]
        for ch in t:
            if ch != '#':
                stk.append([ch, False])
            else:
                if len(stk) != 1:
                    if not stk[-1][1]:
                        stk[-1][1] = True
                    else:
                        while len(stk) > 1 and stk[-1][1]:
                            stk.pop()
                        stk[-1][1] = True
                else:
                    return False

        return len(stk) == 1


p = "1,#,#,#,#"
print(Solution().isValidSerialization(p))