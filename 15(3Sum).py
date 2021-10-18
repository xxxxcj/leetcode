class Solution:
    def threeSum(self, nums: list):
        if len(nums) < 3:
            return []
        nums.sort()
        print(nums)
        ans = []
        nums_len = len(nums)
        i = 0
        i_tmp = nums[0] - 1
        while i < nums_len - 2:
            if nums[i] != i_tmp:
                i_tmp = nums[i]
                j = i + 1
                k = nums_len - 1
                j_tmp = nums[j] - 1
                k_tmp = nums[k] + 1
                while k - j > 0:
                    complement = - nums[i] - nums[j]
                    if j_tmp != nums[j]:
                        if nums[k] != k_tmp:
                            if nums[k] == complement:
                                ans += [[nums[i], nums[j], nums[k]]]
                                k_tmp = nums[k]
                                j_tmp = nums[j]
                                j += 1
                            elif nums[k] > complement:
                                k -= 1
                            else:
                                j += 1
                        else:
                            k -= 1
                    else:
                        j += 1
            i += 1
        return ans


nums = [1,-1,-1,2]
print(Solution().threeSum(nums))
