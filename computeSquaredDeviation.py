def square_deviation(nums: list):
    mean = sum(nums) / len(nums)
    for i in range(len(nums)):
        nums[i] = (nums[i] - mean) ** 2
    return sum(nums)


nums = [0.5, 0.8, 1.1, 1.5, 1.6, 2]
p = 2


def find_min_squared_deviation(nums, p):
    dp = [[square_deviation(nums[i:j]) for i in range(len(nums)) if j - i >= p] for j in range(len(nums)+1)]
    for i in dp:
        print(i)

find_min_squared_deviation(nums, p)