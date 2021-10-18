class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        left, right = 0, len(nums) - 1
        ans = [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            print(left, mid, right)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                a, b = mid - 1, mid + 1
                while True:
                    if a >= 0 and nums[a] == target:
                        a -= 1
                    else:
                        break
                while True:
                    if b <= len(nums) - 1 and nums[b] == target:
                        b += 1
                    else:
                        break
                ans = [a + 1, b - 1]
                break
        return ans


nums = [2,2]
target = 2
print(Solution().searchRange(nums, target))
