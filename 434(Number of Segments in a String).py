class Solution:
    def countSegments(self, s: str) -> int:
        seg = s.split(' ')
        ans = 0
        for i in seg:
            if i != '':
                ans += 1
        return ans


sol = Solution()
print(sol.countSegments('  '))
