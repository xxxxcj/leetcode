class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 逆向双指针可以让空间复杂度降到O(1)
        i, j, k = 0, 0, 0
        tmp = nums1.copy()
        while i < m and j < n:
            if tmp[i] < nums2[j]:
                nums1[k] = tmp[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1

        for t in range(i, m):
            nums1[k] = tmp[t]
            k += 1

        for t in range(j, n):
            nums1[k] = nums2[t]
            k += 1

