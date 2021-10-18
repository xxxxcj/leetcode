class Solution:
    def findSubsequences(self, nums: list) -> list:
        ans = []
        nums_len = len(nums)

        def get_permutation(pre, start):
            if len(pre) > 1:
                ans.append(pre)
            if start == nums_len:
                return
            else:
                for i in range(nums_len - start):
                    if start + i - 1 >= 0 and len(pre) != 0 and nums[start + i] == nums[start + i - 1] and nums[start + i] != pre[-1]:
                        continue
                    if len(pre) == 0 or nums[start + i] >= pre[-1]:
                        get_permutation(pre + [nums[start + i]], start + i + 1)

        get_permutation([], 0)

        return ans


nums = [4,3,2,1,2,3,4]
print(Solution().findSubsequences(nums))
