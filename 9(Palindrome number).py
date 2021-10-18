class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        这个反转数字要注意溢出（python貌似没有这个问题）
        :param x:
        :return:
        if x < 0:
            return False
        if self.reverse(x) == x:
            return True
        else:
            return False

    def reverse(self, x: int):
        ans = 0
        while x > 0:
            ans = ans*10 + x%10
            x = x//10
        return ans
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversenum = 0
        while x > reversenum:
            reversenum = reversenum * 10 + x % 10
            x = x // 10
            # print(x, reversenum)
        return reversenum == x or x == reversenum // 10

x = 10
print(Solution().isPalindrome(x))
