class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacci_numbers = [1, 1]
        while fibonacci_numbers[-1] + fibonacci_numbers[-2] < k:
            fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])

        ans, i = 0, len(fibonacci_numbers)
        while k >= 0:
            if fibonacci_numbers[i] <= k:
                k -= fibonacci_numbers[i]
                ans += 1
            i -= 1
        return ans