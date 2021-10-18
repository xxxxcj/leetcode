class Solution:
    def nextGreaterElements(self, nums: list) -> list:
        # 单调栈
        n = len(nums)
        stk = []
        result = [-1 for _ in range(n)]

        for i in range(n*2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                result[stk.pop()] = nums[i % n]  # 只有循环的最后一次更新是对的，但是总共进行2*n-1次， 所以n个元素都会更新到
            stk.append(i % n)  # 比下标为i%n的数小的都pop出去了

        return result


nums = [1, 2, 1]
print(Solution().nextGreaterElements(nums))