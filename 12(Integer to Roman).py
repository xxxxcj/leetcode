class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        ans = ""
        times = 1
        while num > 0:
            remainder = num % 10
            if remainder < 4:
                for i in range(remainder):
                    ans = int_to_roman[1*times] + ans
            elif remainder == 4:
                ans = int_to_roman[1*times] + int_to_roman[5*times] + ans
            elif remainder == 5:
                ans = int_to_roman[5*times] +ans
            elif 5 < remainder < 9:
                for i in range(remainder - 5):
                    ans = int_to_roman[1*times] + ans
                ans = int_to_roman[5*times] + ans
            else:
                ans = int_to_roman[1*times] + int_to_roman[10*times] + ans
            num //= 10
            times *= 10
        return ans


num = 4
print(Solution().intToRoman(num))
