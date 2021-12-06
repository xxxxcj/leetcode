class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        s = list(enumerate(score))
        s.sort(key=lambda x: x[1], reverse=True)
        ranks = ["" for _ in range(len(score))]
        for idx, item in enumerate(s):
            if idx == 0:
                ranks[item[0]] = "Gold Medal"
            elif idx == 1:
                ranks[item[0]] = "Silver Medal"
            elif idx == 2:
                ranks[item[0]] = "Bronze Medal"
            else:
                ranks[item[0]] = f"{idx+1}"
        return ranks


score = [10, 3, 8, 9, 4]
sol = Solution()
print(sol.findRelativeRanks(score))
