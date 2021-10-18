class Solution:
    def addToArrayForm(self, A: list, K: int) -> list:
        K_list = []
        while K > 0:
            K_list.append(K % 10)
            K //= 10
        K_list.reverse()

        carry = 0
        A_idx = len(A) - 1
        K_idx = len(K_list) - 1
        result = []
        while A_idx >= 0 and K_idx >= 0:
            b = A[A_idx] + K_list[K_idx] + carry
            if b > 9:
                carry = 1
            else:
                carry = 0
            result.append(b % 10)
            A_idx -= 1
            K_idx -= 1

        while A_idx >= 0:
            b = A[A_idx] + carry
            if b > 9:
                carry = 1
            else:
                carry = 0
            result.append(b % 10)
            A_idx -= 1

        while K_idx >= 0:
            b = K_list[K_idx] + carry
            if b > 9:
                carry = 1
            else:
                carry = 0
            result.append(b % 10)
            K_idx -= 1

        if carry != 0:
            result.append(carry)

        result.reverse()
        return result


A = [9,9,9,9,9,9,9,9,9,9]
K = 1
sol = Solution()
print(sol.addToArrayForm(A, K))
