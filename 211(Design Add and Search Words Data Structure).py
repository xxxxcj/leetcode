class Tree:
    def __init__(self):
        self.nodes = [-1 for _ in range(26)]
        self.stop = False


class WordDictionary:

    def __init__(self):
        self.word_tree = Tree()

    def addWord(self, word: str) -> None:
        def add_word_to_tree(word, i, root):
            if i != len(word):
                if root.nodes[ord(word[i]) - ord('a')] == -1:
                    root.nodes[ord(word[i]) - ord('a')] = Tree()
                add_word_to_tree(word, i + 1, root.nodes[ord(word[i]) - ord('a')])
            else:
                root.stop = True
                return
        add_word_to_tree(word, 0, self.word_tree)

    def search(self, word: str) -> bool:
        def search_possible(word, i, root):
            if i != len(word):
                if word[i] == ".":
                    flag = False
                    for _ in range(26):
                        if root.nodes[_] != -1:
                            flag = flag or search_possible(word, i + 1, root.nodes[_])
                    return flag
                else:
                    if root.nodes[ord(word[i]) - ord('a')] == -1:
                        return False
                    return search_possible(word, i + 1, root.nodes[ord(word[i]) - ord('a')])
            else:
                return root.stop

        return search_possible(word, 0, self.word_tree)


# Your WordDictionary object will be instantiated and called as such:
word = "bad"
word2 = ".ad"
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(word2)
print(param_2)
