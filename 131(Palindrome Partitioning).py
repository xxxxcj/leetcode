class Solution:
    def partition(self, s: str) -> list:
        n = len(s)
        is_palindrome = [[True for _ in range(n)] for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and (s[i] == s[j])

        result = []
        ans = []

        def dfs(i: int):
            if i == n:
                result.append(ans.copy())
                return

            for j in range(i, n):
                if is_palindrome[i][j]:
                    ans.append(s[i:j + 1])
                    dfs(j + 1)
                    ans.pop()  # 回溯法  需要还原

        dfs(0)

        return result


s = 'aab'
print(Solution().partition(s))