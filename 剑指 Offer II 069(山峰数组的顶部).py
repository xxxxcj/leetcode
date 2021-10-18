class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1
        mid = 0
        while left <= right:
            mid = (right + left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return mid


arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
sol = Solution()
print(sol.peakIndexInMountainArray(arr))
