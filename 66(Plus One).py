class Solution:
    def plusOne(self, digits: list) -> list:
        tmp = 0
        for i in range(len(digits)-1, -1, -1):
            tmp = digits[i] + 1
            digits[i] = tmp % 10
            if tmp < 10:
                break
        if tmp > 9:
            digits.insert(0, 1)
        return digits