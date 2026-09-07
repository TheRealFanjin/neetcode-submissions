class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = set()
        for i in nums:
            if i in record:
                return True
            record.add(i)
        return False
         