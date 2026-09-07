class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        res = []
        for num in nums:
            freq[num] += 1
        for key, val in freq.items():
            buckets[val].append(key)
        for i in range(len(nums), 0, -1):
            if buckets[i]:
                res.extend(buckets[i])
                if len(res) == k:
                    break
        return res