class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_dict = {}
        for idx, num in enumerate(nums):
            if num not in num_dict:
                num_dict[num] = idx
            else:
                if idx - num_dict[num] <= k:
                    return True
                else:
                    num_dict[num] = idx
        return False
