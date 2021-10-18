class Solution:
    def maxSatisfied(self, customers: list, grumpy: list, X: int) -> int:
        extra = 0
        result = 0
        for i in range(X):
            if grumpy[i]:
                extra += customers[i]
            else:
                result += customers[i]

        max_extra = extra
        for i in range(X, len(customers)):
            if grumpy[i - X]:
                extra -= customers[i-X]

            if grumpy[i]:
                extra += customers[i]
            else:
                result += customers[i]

            if max_extra < extra:
                max_extra = extra

        return result + max_extra


customers = [4,10,10]
grumpy = [1,1,0]
X = 2
print(Solution().maxSatisfied(customers, grumpy, X))