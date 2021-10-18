class Solution:
    def removeDuplicates(self, S: str) -> str:
        # n = len(S)
        # removal = [False for _ in range(n)]
        #
        # def get_next(i):
        #     for j in range(i+1, n):
        #         if not removal[j]:
        #             return j
        #     return -1
        #
        # def get_last(i):
        #     for j in range(i-1, -1, -1):
        #         if not removal[j]:
        #             return j
        #     return -1
        #
        # def remove(i):
        #     if i < n:
        #         if removal[i]:
        #             remove(i + 1)
        #             return
        #         j = get_next(i)
        #         if j != -1:
        #             if S[i] == S[j]:
        #                 removal[i] = removal[j] = True
        #                 t = get_last(i)
        #                 if t >= 0:
        #                     remove(t)
        #                 else:
        #                     remove(j + 1)
        #             else:
        #                 remove(j)
        #
        # remove(0)
        #
        # result = ''
        # for i in range(n):
        #     if not removal[i]:
        #         result += S[i]
        #
        # return result

        # 用栈实现
        result = list()
        n = len(S)

        for i in range(n):
            if len(result) != 0 and S[i] == result[-1]:
                result.pop()
            else:
                result.append(S[i])

        return "".join(result)


s = "ibfjcaffccadidiaidchakchchcahabhibdcejkdkfbaeeaecdjhajbkfebebfea"
print(Solution().removeDuplicates(s))