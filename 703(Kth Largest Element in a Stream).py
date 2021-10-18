class KthLargest:

    def __init__(self, k: int, nums: list):
        self.k = k - 1
        self.nums = nums
        self.nums.sort(reverse=True)

    def add(self, val: int) -> int:
        if len(self.nums) == 0 or val <= self.nums[-1]:
            self.nums.append(val)
            return self.nums[self.k]
        if val >= self.nums[0]:
            self.nums.insert(0, val)
            return self.nums[self.k]

        left, right = 0, len(self.nums)
        while True:
            i = (left + right) // 2
            if self.nums[i] >= val > self.nums[i + 1]:
                self.nums.insert(i + 1, val)
                break
            if val > self.nums[i]:
                right = i
            else:
                left = i
        return self.nums[self.k]


inst = ["KthLargest", "add", "add", "add", "add", "add"]
data = [[1, []], [-3], [-2], [-4], [0], [4]]

sol = KthLargest(data[0][0], data[0][1])

result = [None, ]
for num in data[1:]:
    result.append(sol.add(num[0]))

print(result)
