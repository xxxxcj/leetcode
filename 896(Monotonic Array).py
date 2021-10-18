class Solution:
    def isMonotonic(self, A: list) -> bool:
        # n = len(A)
        #
        # i = 0
        # while i < n - 1:
        #     if A[i] < A[i + 1]:
        #         is_increasing = True
        #         break
        #     if A[i] > A[i + 1]:
        #         is_increasing = False
        #         break
        #     i += 1
        #
        # if i == n-1:
        #     return True
        # if is_increasing:
        #     for j in range(i + 1, n - 1):
        #         if A[j] > A[j + 1]:
        #             return False
        # else:
        #     for j in range(i + 1, n - 1):
        #         if A[j] < A[j + 1]:
        #             return False
        #
        # return True

        n = len(A)
        diff = []
        for i in range(n - 1):
            diff.append(A[i] - A[i+1])

        i = 0
        while i < len(diff):
            if diff[i] != 0:
                break
            i += 1

        for d in diff[i + 1:]:
            if d*diff[i] < 0:
                return False

        return True


A = [1, 1]
print(Solution().isMonotonic(A))
