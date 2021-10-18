class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        def add(a:str, b:str):
            a_len, b_len = len(a), len(b)
            if a_len > b_len:
                b = '0'*(a_len - b_len) + b
            else:
                a = '0'*(b_len - a_len) + a

            carry = 0
            sol = ''
            i = max(a_len, b_len) - 1
            while i >= 0:
                sum = int(a[i]) + int(b[i]) + carry
                remainder = sum % 10
                carry = sum // 10
                sol = str(remainder) + sol
                i -= 1
            if carry != 0:
                sol = str(carry) + sol
            return sol

        def single_multiply(a:str, b:str):  # a为一位， b为多位
            carry = 0
            sol = ""
            i = len(b) - 1
            while i >= 0:
                x = int(a)*int(b[i]) + carry
                remainder = x % 10
                carry = x // 10
                sol = str(remainder) + sol
                i -= 1
            if carry != 0:
                sol = str(carry) + sol
            return sol

        sol = ""
        num1_len = len(num1)
        i = num1_len - 1
        while i >= 0:
            sol = add(sol, single_multiply(num1[i], num2) + '0'*(num1_len - i - 1))
            i -= 1

        i = 0
        while i < len(sol) - 1 and sol[i] == '0':
            i += 1

        return sol[i:]


num1 = "9133"
num2 = "0"
print(Solution().multiply(num1, num2))
