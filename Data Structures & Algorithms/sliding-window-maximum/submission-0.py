class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        nums_set = defaultdict(int)
        for i in range(k):
            heapq.heappush(heap, -nums[i])
            nums_set[nums[i]] += 1
        res.append(-heap[0])
        l,r = 0,k - 1
        while r < len(nums) - 1:
            r += 1
            heapq.heappush(heap, -nums[r])
            nums_set[nums[r]] += 1
            nums_set[nums[l]] -= 1
            if not nums_set[nums[l]]:
                nums_set.pop(nums[l])
            if nums[l] == -heap[0]:
                while -heap[0] not in nums_set:
                    heapq.heappop(heap)
            l += 1
            res.append(-heap[0])
        return res
                
        