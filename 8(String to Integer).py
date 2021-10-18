class Solution:
    def myAtoi(self, str: str) -> int:
        MAX = 2 ** 31 - 1
        MIN = -2 ** 31
        front = 0
        ans = 0
        sign = True
        for i in str:
            if i == " ":
                front += 1
            else:
                break
        if front == len(str):
            return 0
        if str[front] == "-":
            sign = False
            front += 1
        elif str[front] == "+":
            front += 1
        str = str[front:]
        for i in str:
            if "0" <= i <= "9":
                ans = ans * 10 + int(i)
            else:
                break
        ans = ans if sign else -ans
        if MIN <= ans <= MAX:
            return ans
        elif ans < MIN:
            return MIN
        else:
            return MAX


str = " -42"
print(Solution().myAtoi(str))
