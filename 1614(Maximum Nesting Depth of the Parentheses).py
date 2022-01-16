class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0
        for ch in s:
            if ch == "(":
                depth += 1
                max_depth = max(depth, max_depth)
            elif ch == ")":
                depth -= 1
        return max_depth


s = "(1+(2*3)+((8)/4))+1"
sol = Solution()
print(sol.maxDepth(s))