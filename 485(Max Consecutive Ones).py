class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        max_len = 0
        l = 0
        for i in nums:
            if i:
                l += 1
            else:
                if max_len < l:
                    max_len = l
                l = 0
        if max_len < l:
            max_len = l
        return max_len
