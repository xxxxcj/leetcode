# class Solution:
#     def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
#         num_requests = [0 for _ in range(k)]
#         servers = [0 for _ in range(k)]
#
#         def find_available(idx, request):
#             i = idx
#             num_s = 0
#             while servers[i % k] > request and num_s < k:
#                 i += 1
#                 num_s += 1
#
#             if num_s == k:
#                 return -1
#             else:
#                 return i % k
#
#         for idx, arrival_time in enumerate(arrival):
#             avail_server = find_available(idx, arrival_time)
#             if avail_server != -1:
#                 num_requests[avail_server] += 1
#                 servers[avail_server] = arrival_time + load[idx]
#
#         ans = [0]
#         for idx, n in enumerate(num_requests[1:]):
#             if n > num_requests[ans[0]]:
#                 ans = [idx + 1]
#             elif n == num_requests[ans[0]]:
#                 ans.append(idx + 1)
#
#         return ans

from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        requests = [0] * k
        for i, (start, t) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                available.add(busy[0][1])
                heappop(busy)
            if len(available) == 0:
                continue
            j = available.bisect_left(i % k)
            if j == len(available):
                j = 0
            id = available[j]
            requests[id] += 1
            heappush(busy, (start + t, id))
            available.remove(id)
        maxRequest = max(requests)
        return [i for i, req in enumerate(requests) if req == maxRequest]


k = 3
arrival = [1, 2, 3, 4]
load = [1, 2, 1, 2]
sol = Solution()
print(sol.busiestServers(k, arrival, load))
