class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stone_heap = []
        for stone in stones:
            heapq.heappush(stone_heap, -stone)
        
        while len(stone_heap) > 1:
            stone1, stone2 = -heapq.heappop(stone_heap), -heapq.heappop(stone_heap)
            if stone1 != stone2:
                heapq.heappush(stone_heap, -(stone1 - stone2))
        return -stone_heap[0] if stone_heap else 0