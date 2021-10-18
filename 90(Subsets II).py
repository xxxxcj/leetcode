class Solution:
    def subsetsWithDup(self, nums: list) -> list:
        ret = set()
        n = len(nums)
        nums.sort()
        def dfs(i, subset):
            for j in range(i, n):
                tmp = tuple(subset + [nums[j]])
                if tmp not in ret:
                    ret.add(tmp)
                dfs(j+1, subset + [nums[j]])

        dfs(0, [])

        return list(ret) + [[]]


nums = [1,2,2]
print(Solution().subsetsWithDup(nums))