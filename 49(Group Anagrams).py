import collections


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        ans = collections.defaultdict(list)
        for s in strs:
            counts = [0 for x in range(26)]
            for c in s:
                counts[ord(c)-ord('a')] += 1
            ans[tuple(counts)].append(s)
        return list(ans.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))

