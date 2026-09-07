class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        for i in range(0, len(nums) + 1):
            if i not in s:
                return i