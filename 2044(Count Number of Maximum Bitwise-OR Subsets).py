from queue import Queue


class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_value = 0
        ans = 0
        q = Queue()
        q.put(nums[0])
        q.put(0)

        for i in range(1, len(nums)):
            for j in range(2**i):
                tmp = q.get()
                q.put(tmp)
                tmp = tmp | nums[i]
                q.put(tmp)

        while not q.empty():
            tmp = q.get()
            if tmp > max_value:
                max_value = tmp
                ans = 1
            elif tmp == max_value:
                ans += 1
        return ans


nums = [2,2,2]
sol = Solution()
print(sol.countMaxOrSubsets(nums))
