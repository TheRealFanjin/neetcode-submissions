class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        total = 0
        for num in nums:
            s.add(num)
        for num in nums:
            if num - 1 not in s:
                curr_total = 1
                curr = num
                while curr + 1 in s:
                    curr_total += 1
                    curr += 1
                total = max(curr_total, total)
        return total