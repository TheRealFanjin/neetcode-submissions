class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        counter = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                counter1 = 1
                while nums[i] + counter1 in nums_set:
                    counter1 += 1
                if counter1 > counter:
                    counter = counter1
        return counter
        