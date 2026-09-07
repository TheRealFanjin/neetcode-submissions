class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set()
        idx_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in s:
                return [idx_dict[target - nums[i]], i]
            s.add(nums[i])
            idx_dict[nums[i]] = i