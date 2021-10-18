class Solution:
    def maxArea(self, height: list) -> int:
        '''
        双指针法 复杂度O（N）  leetcode官方解法
        i, j = 0, len(height) - 1
        ans = 0
        while i != j and i < j:
            ans_tmp = min(height[i], height[j])*(j - i)
            if ans_tmp > ans:
                ans = ans_tmp
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                i += 1
                j -= 1
        return ans
        '''
        # 暴力膜法
        ans = 0
        i = 0
        height_len = len(height)
        while i < height_len:
            j = i + 1
            while j < height_len:
                ans_tmp = min(height[i], height[j])*(j - i)
                if ans_tmp > ans:
                    ans = ans_tmp
                j += 1
            i += 1
        return ans


height = [1, 8, 6, 2, 5, 4, 8, 3, 7, 1]
print(Solution().maxArea(height))
