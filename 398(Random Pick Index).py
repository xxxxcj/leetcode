import random


class Solution:

    def __init__(self, nums: list[int]):
        self.indices = {}

        for idx, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = [idx]
            else:
                self.indices[num].append(idx)

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
