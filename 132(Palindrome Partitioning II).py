class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        palindrome = [[True for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                palindrome[i][j] = palindrome[i+1][j-1] and (s[i] == s[j])

        cut_num = [n for _ in range(n)]
        for i in range(n):
            if palindrome[0][i]:
                cut_num[i] = 0  # 如果到第i是回文，那么分割数就是0
            else:
                for j in range(i):
                    if palindrome[j + 1][i]:
                        cut_num[i] = min(cut_num[i], cut_num[j] + 1)

        return cut_num[n-1]


s = 'aaabaa'
print(Solution().minCut(s))