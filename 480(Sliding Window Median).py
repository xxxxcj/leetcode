class Solution:
    # 用堆时间复杂度更低找中位数  如下为暴力方法
    def medianSlidingWindow(self, nums: list, k: int) -> list:
        def get_median(window_nums):
            if k % 2:
                return window_nums[k // 2]
            else:
                return (window_nums[k // 2 - 1] + window_nums[k // 2]) / 2

        def insert_num(w: list, num):
            for i in range(k - 1):
                if w[i] > num:
                    w.insert(i, num)
                    return
            w.append(num)

        window = nums[0: k]
        medians = []

        window.sort()
        medians.append(get_median(window))
        for i in range(len(nums) - k):
            num = nums[k + i]
            remove_num = nums[i]
            window.remove(remove_num)
            insert_num(window, num)
            medians.append(get_median(window))

        return medians


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().medianSlidingWindow(nums, k))
