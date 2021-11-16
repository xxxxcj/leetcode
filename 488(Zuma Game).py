class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def step(board, ch, i):
            li = []
            for j in range(len(board)):
                if j == i:
                    li.append(ch)
                li.append(board[j])
                



        def dfs(board, hand, i):
            for idx, item in enumerate(hand):
                for j in range(len(board)+1):
