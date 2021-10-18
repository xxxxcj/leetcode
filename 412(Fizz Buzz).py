class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        ans = list()
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    ans.append("FizzBuzz")
                else:
                    ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans