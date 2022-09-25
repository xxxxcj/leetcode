class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        n = len(words)
        ans = {}
        for i in range(n):
            for j in range(i+1, n):
                if len(words[i]) < len(words[j]):
                    reversed_str = words[i].split()
                    reversed_str.reverse()
                    reversed_str = "".join(reversed_str)
                    if words[j].find(words[i]) != -1 or words[j].find(reversed_str) != -1:
                        if words[i] not in ans:
                            ans[words[i]] = 1
                elif len(words[i]) > len(words[j]):
                    reversed_str = words[j].split()
                    reversed_str.reverse()
                    reversed_str = "".join(reversed_str)
                    if words[i].find(words[j]) != -1 or words[i].find(reversed_str) != -1:
                        if words[j] not in ans:
                            ans[words[j]] = 1
        return list(ans.keys())
