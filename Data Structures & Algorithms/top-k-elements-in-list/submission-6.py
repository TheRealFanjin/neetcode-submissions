from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        
        l = [(-j, i) for i,j in frequency.items()]
        heapq.heapify(l)
        output = []
        for i in range(k):
            output.append(heapq.heappop(l)[1])
        return output

        