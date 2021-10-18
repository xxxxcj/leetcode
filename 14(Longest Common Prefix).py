class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        strs_len = len(strs)
        if strs_len == 0:
            return ""
        min_len = len(strs[0])
        for i in strs[1:]:
            i_len = len(i)
            if i_len < min_len:
                min_len = i_len
        j = 0
        flag = True
        ans = ""
        while j < min_len:
            tmp = strs[0][j]
            i = 1
            while i < strs_len:
                if strs[i][j] != tmp:
                    flag = False
                    break
                i += 1
            if flag:
                ans += tmp
            else:
                break
            j += 1
        return ans


strs = []
print(Solution().longestCommonPrefix(strs))
