class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        distance = []
        for i in range(len(s)):
            distance.append(abs(ord(s[i]) - ord(t[i])))
        i = 0
        sum_dist = 0
        for j in range(len(s)):
            sum_dist += distance[j]
            if sum_dist > maxCost:
                sum_dist -= distance[i]
                i += 1

        return len(s) - i


s = "abcd"
t = "bcdf"
maxCost = 3

print(Solution().equalSubstring(s, t, maxCost))
