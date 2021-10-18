class Solution:
    def maxScore(self, cardPoints: list, k: int) -> int:
        j = len(cardPoints) - k
        sum_of_points = sum(cardPoints[j:])
        max_sum_of_points = sum_of_points
        for i in range(k):
            sum_of_points = sum_of_points + cardPoints[i] - cardPoints[j]
            if sum_of_points > max_sum_of_points:
                max_sum_of_points = sum_of_points
            j += 1

        return max_sum_of_points
