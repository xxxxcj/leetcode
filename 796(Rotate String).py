class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            j = 0
            while j < len(s):
                if s[(i+j) % len(s)] != goal[j]:
                    break
                j += 1
            if j == len(s):
                return True
        return False


s = "abcde"
goal = "abced"
sol = Solution()
print(sol.rotateString(s, goal))