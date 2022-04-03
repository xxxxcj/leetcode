class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def is_self_dividing_num(num: int):
            n = num
            while n != 0:
                a = n % 10
                n //= 10
                if a == 0 or num % a != 0:
                    return False
            return True

        ans = []
        for i in range(left, right+1):
            if is_self_dividing_num(i):
                ans.append(i)

        return ans


left = 1
right = 22
sol = Solution()
print(sol.selfDividingNumbers(left,right))