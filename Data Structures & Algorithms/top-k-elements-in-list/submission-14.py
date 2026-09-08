class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_group = [[] for _ in range(len(nums))]
        freq_dict = defaultdict(int)
        for num in nums:
            freq_dict[num] += 1
        for key, val in freq_dict.items():
            freq_group[val - 1].append(key)
        res = []
        count = 0
        idx = -1
        while count < k:
            if freq_group[idx]:
                res.extend(freq_group[idx])
                count += len(freq_group[idx])
            idx -= 1
        return res