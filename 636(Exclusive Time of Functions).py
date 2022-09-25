class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        ans = [0 for _ in range(n)]
        stk = []
        for log in logs:
            log = log.split(":")
            log[0] = int(log[0])
            log[2] = int(log[2])
            if log[1] == "end":
                ans[log[0]] += log[2] + 1 - stk[-1][2]
                stk.pop()
                if stk:
                    stk[-1][2] = log[2] + 1
            else:
                if stk:
                    ans[stk[-1][0]] += log[2] - stk[-1][2]
                    stk[-1][2] = log[2]
                stk.append(log)
        return ans



n = 8
logs = ["0:start:0", "1:start:5", "2:start:6", "3:start:9", "4:start:11", "5:start:12", "6:start:14", "7:start:15",
        "1:start:24", "1:end:29", "7:end:34", "6:end:37", "5:end:39", "4:end:40", "3:end:45", "0:start:49", "0:end:54",
        "5:start:55", "5:end:59", "4:start:63", "4:end:66", "2:start:69", "2:end:70", "2:start:74", "6:start:78",
        "0:start:79", "0:end:80", "6:end:85", "1:start:89", "1:end:93", "2:end:96", "2:end:100", "1:end:102",
        "2:start:105", "2:end:109", "0:end:114"]
print(Solution().exclusiveTime(n, logs))
