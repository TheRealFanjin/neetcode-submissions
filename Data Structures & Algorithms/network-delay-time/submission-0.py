from math import inf
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for (source, target, time) in times:
            adj[source - 1].append((target - 1, time))
        dist = [inf] * n
        pq = [(0, k - 1)]
        dist[k - 1] = 0

        while pq:
            d, u = heapq.heappop(pq)
            for (v, time) in adj[u]:
                if dist[v] > dist[u] + time:
                    dist[v] = dist[u] + time
                    heapq.heappush(pq, (dist[v], v))
        min_time = -1
        for dis in dist:
            if dis == inf:
                return -1
            if dis > min_time:
                min_time = dis
        return min_time