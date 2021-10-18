class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        n, m = len(a), len(b)

        i, j = n-1, m-1
        result = []
        while i >= 0 and j >= 0:
            binary_sum = carry + int(a[i]) + int(b[j])
            result.append(binary_sum % 2)
            carry = binary_sum//2
            i -= 1
            j -= 1

        if i == -1:
            while j >= 0:
                binary_sum = carry + int(b[j])
                result.append(binary_sum % 2)
                carry = binary_sum // 2
                j -= 1

        if j == -1:
            while i >= 0:
                binary_sum = carry + int(a[i])
                result.append(binary_sum % 2)
                carry = binary_sum // 2
                i -= 1

        if carry != 0:
            result.append(carry)

        result_str = ""
        for i in range(len(result)-1, -1, -1):
            result_str += str(result[i])

        return result_str


a = "1"
b = "111"
print(Solution().addBinary(a, b))