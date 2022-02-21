class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (right + left) // 2
            if nums[mid] == nums[mid + 1]:
                if (right - mid + 1) % 2 == 0:
                    right = mid - 1
                else:
                    left = mid + 2
            elif nums[mid] == nums[mid - 1]:
                if (right - mid) % 2 == 0:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]

        return nums[left]


nums = [1,1,2]
sol = Solution()
print(sol.singleNonDuplicate(nums))
