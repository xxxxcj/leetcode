class NumArray:

    def __init__(self, nums: list):
        self.sum_0j = [0]
        for num in nums:
            self.sum_0j.append(self.sum_0j[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum_0j[j+1] - self.sum_0j[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)