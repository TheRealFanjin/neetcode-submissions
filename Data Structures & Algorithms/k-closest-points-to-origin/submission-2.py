class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (point_x, point_y) in points:
            distance = math.sqrt((point_x) ** 2 + (point_y) ** 2)
            heapq.heappush(heap, (distance, point_x, point_y))
        res = []
        for i in range(k):
            coords = heapq.heappop(heap)
            res.append([coords[1], coords[2]])
        return res