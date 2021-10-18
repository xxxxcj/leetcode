class Solution:
    def sortedSquares(self, A: list) -> list:
        # square_sorted_list = []
        # mid = 0
        # for i in range(1, len(A)):
        #     if A[i-1] < 0 and A[i] >= 0:
        #         mid = i
        # left, right = mid - 1, mid
        # while left >= 0 and right < len(A):
        #     if A[left]*A[left] < A[right]*A[right]:
        #         square_sorted_list.append(A[left]*A[left])
        #         left -= 1
        #     else:
        #         square_sorted_list.append(A[right] * A[right])
        #         right += 1
        #
        # if left == -1:
        #     while right < len(A):
        #         square_sorted_list.append(A[right] * A[right])
        #         right += 1
        # else:
        #     while left >= 0:
        #         square_sorted_list.append(A[left] * A[left])
        #         left -= 1
        # return square_sorted_list
        left = 0
        right = len(A) - 1

        while left <= right:
            mid = (left + right) // 2
            if A[mid] == 0:
                left = mid
                break
            elif A[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1

        neg_p = left - 1
        pos_p = left

        ans = list()
        while neg_p > -1 and pos_p < len(A):
            neg_square = A[neg_p] * A[neg_p]
            pos_square = A[pos_p] * A[pos_p]

            if neg_square < pos_square:
                ans.append(neg_square)
                neg_p -= 1
            elif neg_square > pos_square:
                ans.append(pos_square)
                pos_p += 1
            else:
                ans.append(pos_square)
                ans.append(neg_square)
                pos_p += 1
                neg_p -= 1

        if neg_p > -1:
            for i in range(neg_p, -1, -1):
                ans.append(A[i] * A[i])

        if pos_p < len(A):
            for i in range(pos_p, len(A)):
                ans.append(A[i] * A[i])

        return ans


A = [-4, -1, 0, 3, 10]
sol = Solution()
print(sol.sortedSquares(A))
