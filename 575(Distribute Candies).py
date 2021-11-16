class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        candy_dict = {}
        for i in candyType:
            if i not in candy_dict:
                candy_dict[i] = 1
            else:
                candy_dict[i] += 1

        return min(len(candyType)//2, len(candy_dict))