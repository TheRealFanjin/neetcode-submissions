import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[math.sqrt(points[i][0] ** 2 + points[i][1] ** 2), i] for i in range(len(points))]
        heapq.heapify(distances)
        res = []
        for _ in range(k):
            res.append(points[heapq.heappop(distances)[1]])
        return res
