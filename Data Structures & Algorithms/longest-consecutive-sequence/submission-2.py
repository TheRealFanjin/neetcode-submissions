class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums_set:
                counter = 1
                for i in range(len(nums_set)):
                    if num + counter in nums_set:
                        counter += 1
                    else:
                        break
                if counter > longest:
                    longest = counter
        return longest