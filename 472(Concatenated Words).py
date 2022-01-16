class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

    def insert(self, word: str):
        node = self
        for ch in word:
            order = ord(ch) - ord('a')
            if node.children[order] is None:
                node.children[order] = Trie()
            node = node.children[order]
        node.isEnd = True

    def dfs(self, word: str, start: int):
        if start == len(word):
            return True
        node = self
        for i in range(start, len(word)):
            node = node.children[ord(word[i]) - ord('a')]
            if node is None:
                return False
            if node.isEnd and self.dfs(word, i + 1):
                return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        words.sort(key=lambda x: len(x))

        trie = Trie()
        ans = []
        for word in words:
            if word == "":
                continue
            if trie.dfs(word, 0):
                ans.append(word)
            else:
                trie.insert(word)
        return ans
