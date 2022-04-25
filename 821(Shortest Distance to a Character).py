class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        occurrence = []

        for idx, ch in enumerate(s):
            if ch == c:
                occurrence.append(idx)

        ans = []
        for i in range(len(occurrence)):
            if i == 0:
                for j in range(occurrence[i]):
                    ans.append(occurrence[i] - j)
            else:
                for j in range(occurrence[i - 1], occurrence[i]):
                    ans.append(min(j - occurrence[i - 1], occurrence[i] - j))

        for j in range(occurrence[-1], len(s)):
            ans.append(j - occurrence[- 1])

        return ans


s = "abaa"
c = "b"
print(Solution().shortestToChar(s, c))
