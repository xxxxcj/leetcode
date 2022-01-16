class Solution:
    def simplifyPath(self, path: str) -> str:
        file_names = path.split('/')
        res = []

        for name in file_names:
            if name != "":
                if name != '.':
                    if name == '..':
                        if len(res) >= 1:
                            res = res[:-1]
                    else:
                        res.append(name)

        ans = ""
        for name in res:
            ans += '/'
            ans += name

        if len(res) == 0:
            ans += '/'

        return ans


path = "/home/"
sol = Solution()
print(sol.simplifyPath(path))
