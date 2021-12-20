import heapq


class Solution:
    def scheduleCourse(self, courses: list) -> int:
        courses.sort(key=lambda c: c[1])

        q = list()
        # 优先队列中所有课程的总时间
        total = 0

        for ti, di in courses:
            if total + ti <= di:
                total += ti
                # Python 默认是小根堆
                heapq.heappush(q, -ti)
            elif q and -q[0] > ti:
                total -= -q[0] - ti
                heapq.heappop(q)
                heapq.heappush(q, -ti)

        return len(q)


courses = [[5, 5], [4, 6], [2, 6]]
sol = Solution()
print(sol.scheduleCourse(courses))
