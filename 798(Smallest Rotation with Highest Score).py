class Solution:
    # 超时  可以用差分数组加速
    def bestRotation(self, nums: list[int]) -> int:
        k = [0 for _ in range(len(nums))]

        for idx, num in enumerate(nums):
            if idx >= num:
                for i in range(idx - num + 1):
                    k[i] += 1
                for i in range(idx + 1, len(nums)):
                    k[i] += 1
            elif num >= len(nums):
                continue
            else:
                for i in range(idx + 1, len(nums) - (num - idx) + 1):
                    k[i] += 1

        max_idx, max_val = 0, 0
        for idx, val in enumerate(k):
            if val > max_val:
                max_val = val
                max_idx = idx

        return max_idx


nums = [2, 3, 1, 4, 0]
print(Solution().bestRotation(nums))
