class Solution:
    def lengthLongestPath(self, input: str) -> int:
        file_sys = input.split('\n')

        stk = []

        max_len = 0
        now_len = 0
        for filename in file_sys:
            depth = filename.count('\t')
            filename = filename[depth:]
            if depth == len(stk):
                stk.append(filename)
                now_len += len(filename) + 1
            else:
                if stk[-1].find('.') != -1:
                    max_len = max(max_len, now_len - 1)
                print(stk, depth, filename)
                while len(stk) != depth:
                    now_len -= len(stk[-1]) + 1
                    stk.pop(-1)
                stk.append(filename)
                now_len += len(filename) + 1
        if stk[-1].find('.') != -1:
            max_len = max(max_len, now_len - 1)
        return max_len


input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(Solution().lengthLongestPath(input))
