class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        h1_size = len(self.heap1)
        h2_size = len(self.heap2)
        if h1_size > h2_size:
            if num <= -self.heap1[0]:
                heapq.heappush(self.heap1, -num)
                heapq.heappush(self.heap2, -heapq.heappop(self.heap1))
            else:
                heapq.heappush(self.heap2, num)
        else:
            if not self.heap1 or num <= -self.heap1[0]:
                heapq.heappush(self.heap1, -num)
            else:
                heapq.heappush(self.heap2, num)
                heapq.heappush(self.heap1, -heapq.heappop(self.heap2))
        

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            return (-self.heap1[0] + self.heap2[0]) / 2
        return -self.heap1[0]
        