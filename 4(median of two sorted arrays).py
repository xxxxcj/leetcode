class Solution(object):
    def findMedianSortedArrays(self, nums1:list, nums2:list):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        """
        方法思想是将nums1和nums2用他们的中位数分表分堆为A1, A2, B1, B2,然后A1 B1合并，A2，B2合并
        如果1堆中的最大值大于2堆中的最小值，就进行交换，然后再比较，最后如果总长为奇数，那就是1堆的最大值
        如果是偶数就是1堆最大值和2堆最小值的均值
        """
        if not nums1:
            return self.__get_median(nums2)[0]
        if not nums2:
            return self.__get_median(nums1)[0]
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        if nums2_len == 1 and nums1_len == 1:
            return (nums1[0] + nums2[0])/2

        p1 = (nums1_len - 1) // 2
        p2 = (nums2_len - 1) // 2

        if nums1_len % 2 and nums2_len % 2:
            if p2 > p1:
                p2 -= 1
            else:
                p1 -= 1
        while True:
            if p2 < nums2_len - 1 and nums1[p1] > nums2[p2 + 1]:
                p2 += 1
                p1 -= 1
            if p1 < nums1_len - 1 and nums2[p2] > nums1[p1 + 1]:
                p1 += 1
                p2 -= 1
            if p1 == -1 or p2 == -1 or p1 == nums1_len - 1 or p2 == nums2_len - 1 or (nums1[p1] <= nums2[p2 + 1] and nums2[p2] <= nums1[p1 + 1]):
                if (nums1_len + nums2_len) % 2:
                    if p1 == -1:
                        return nums2[p2]
                    if p2 == -1:
                        return nums1[p1]
                    return max(nums1[p1], nums2[p2])
                else:
                    if p1 == -1:
                        max_left = nums2[p2]
                    elif p2 == -1:
                        max_left = nums1[p1]
                    else:
                        max_left = max(nums1[p1], nums2[p2])
                    if p1 == nums1_len - 1:
                        min_right = nums2[p2 + 1]
                    elif p2 == nums2_len - 1:
                        min_right = nums1[p1 + 1]
                    else:
                        min_right = min(nums1[p1 + 1], nums2[p2 + 1])
                    return (max_left + min_right) / 2

    def __get_median(self, nums):
        nums_len = len(nums)
        if nums_len % 2:  # 奇数
            return nums[nums_len // 2], nums_len // 2
        else:
            return (nums[nums_len // 2] + nums[nums_len // 2 - 1]) / 2, nums_len / 2 - 0.5

"""
直接sort符合 O(log(m+n))的时间复杂度吗？
可能是因为用于测试的用例比较短
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = list()
        num.extend(nums1)
        num.extend(nums2)
        num.sort()
        m = len(nums1)
        n = len(nums2)
        ret = 0
        if (m + n) % 2 == 0:
            ret = (num[int((m + n) / 2) - 1] + num[int((m + n) / 2)]) / 2
        else:
            ret = (num[(m + n) // 2])
        return ret
"""

nums1 = [4]
nums2 = [1,2, 3 ]
print(Solution().findMedianSortedArrays(nums1,nums2))
