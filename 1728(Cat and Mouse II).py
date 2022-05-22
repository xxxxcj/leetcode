class Solution:
    def canMouseWin(self, grid: list[str], catJump: int, mouseJump: int) -> bool:
        maxIter = 1000
        def play(posCat: list[int], posMouse: list[int], iterNum=0):
