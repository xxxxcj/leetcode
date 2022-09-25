class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
        nums.sort()
        ans = []
        for i in range(n):
            t1 = target - nums[i]
            for j in range(i + 1, n):
                t2 = t1 - nums[j]
                for k in range(j + 1, n - 1):
                    t3 = t2 - nums[k]
                    if t3 == nums[k + 1] or (t3 > nums[k] and t3 in nums_dict):
                        ans_tmp = [nums[i], nums[j], nums[k], t3]
                        if ans_tmp not in ans:
                            ans.append([nums[i], nums[j], nums[k], t3])
        return ans


nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
target = 8
sol = Solution()
print(sol.fourSum(nums, target))
