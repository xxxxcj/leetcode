class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnd = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for ch in word:
            if p.children[ord(ch) - ord('a')] is None:
                p.children[ord(ch) - ord('a')] = TrieNode()
            p = p.children[ord(ch) - ord('a')]
        p.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for ch in word:
            if p.children[ord(ch) - ord('a')] is not None:
                p = p.children[ord(ch) - ord('a')]
            else:
                return False
        return p.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for ch in prefix:
            if p.children[ord(ch) - ord('a')] is not None:
                p = p.children[ord(ch) - ord('a')]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)