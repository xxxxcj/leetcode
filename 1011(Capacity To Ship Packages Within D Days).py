class Solution:
    def shipWithinDays(self, weights: list, D: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2
            count = 1
            convey_once = 0
            for w in weights:
                if convey_once + w > mid:
                    count += 1
                    convey_once = w
                else:
                    convey_once += w
            if count > D:
                left = mid + 1
            else:
                right = mid - 1

        return left


weights = [3, 2, 2, 4, 1, 4]
D = 3
print(Solution().shipWithinDays(weights, D))
