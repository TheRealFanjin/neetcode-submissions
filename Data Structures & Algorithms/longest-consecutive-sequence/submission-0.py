class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        groups = set()
        passed = set()
        longest = 0
        for num in nums:
            groups.add(num)
        for num in nums:
            if num - 1 not in groups and num not in passed:
                check = num
                tempLongest = 0
                while check in groups:
                    tempLongest += 1
                    passed.add(check)
                    check += 1
                if tempLongest > longest:
                    longest = tempLongest
        
        return longest
        