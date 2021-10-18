class Solution:
    def letterCombinations(self, digits: str) -> list:
        if len(digits) == 0:
            return []
        dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "stuv", "9": "wxyz"}
        letters = []
        ans = []
        tmp = ""
        for i in digits:
            letters += [dict[i]]
        self.get_all_solution(letters, 0, ans, tmp, len(letters)-1)
        return ans

    def get_all_solution(self, letters, i, ans, tmp, depth):
        if i == depth:
            for j in letters[i]:
                ans += [tmp+j]
        else:
            for j in letters[i]:
                self.get_all_solution(letters, i+1, ans, tmp+j, depth)



digits = "2"
print(Solution().letterCombinations(digits))
