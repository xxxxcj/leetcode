class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums_len = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        i = 0
        nums.sort()
        while i < nums_len - 2:
            j = i + 1
            k = nums_len - 1
            while k > j:
                print(i, j, k)
                complement = target - nums[i] - nums[j]
                print(complement, nums[i]+nums[j]+nums[k])
                if abs(nums[i] + nums[j] + nums[k] - target) < abs(ans - target):
                    ans = nums[i] + nums[j] + nums[k]
                if complement > nums[k]:
                    j += 1
                elif complement < nums[k]:
                    k -= 1
                else:
                    return target
            i += 1
        return ans


nums = [1,6,9,14,16,70]
target = 81
print(Solution().threeSumClosest(nums, target))
