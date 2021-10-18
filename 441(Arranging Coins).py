class Solution:
    def arrangeCoins(self, n: int) -> int:
        n_coins = 1
        layers = 0
        while n >= n_coins:
            n -= n_coins
            n_coins += 1
            layers += 1
        return layers