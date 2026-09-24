class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        min_cost = 0
        heap = [(0, 0)]

        while len(visited) < len(points):
            dist, point_idx = heapq.heappop(heap)

            if point_idx in visited:
                continue
            min_cost += dist
            visited.add(point_idx)

            for i in range(len(points)):
                if i not in visited:
                    heapq.heappush(heap, (abs(points[point_idx][0] - points[i][0]) + abs(points[point_idx][1] - points[i][1]), i))
        return min_cost