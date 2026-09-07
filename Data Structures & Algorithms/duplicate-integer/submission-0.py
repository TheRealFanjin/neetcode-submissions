class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        record = []
        for i in nums:
            if i in record:
                return True
            else:
                record.append(i)
        return False
         