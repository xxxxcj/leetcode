class Solution:
    def numberToWords(self, num: int) -> str:
        vocabulary = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }

        def num2en_less_than_100(n: int):
            if n <= 20:
                return vocabulary[n]
            if n < 100:
                if not n % 10:
                    return vocabulary[n]
                return vocabulary[n // 10 * 10] + " " + vocabulary[n % 10]

        def num2en_less_than_1000(n: int):
            if n < 100:
                return num2en_less_than_100(n)
            if not n % 100:
                return vocabulary[n // 100] + " Hundred"
            return vocabulary[n // 100] + " Hundred " + num2en_less_than_100(n % 100)

        num1 = num % 1e3
        num2 = num // 1e3 % 1e3
        num3 = num // 1e6 % 1e3
        num4 = num // 1e9

        if num2 == num3 == num4 == 0:
            return num2en_less_than_1000(num1)

        ans = ""
        if num4 != 0:
            ans += " " + num2en_less_than_1000(num4) + " Billion"

        if num3 != 0:
            ans += " " + num2en_less_than_1000(num3) + " Million"

        if num2 != 0:
            ans += " " + num2en_less_than_1000(num2) + " Thousand"

        if num1 != 0:
            ans += " " + num2en_less_than_1000(num1)

        return ans[1:]


sol = Solution()
print(sol.numberToWords(1234567891))
