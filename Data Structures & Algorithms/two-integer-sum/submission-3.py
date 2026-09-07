class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test = {}
        for i in range(len(nums)):
            if target - nums[i] in test:
                return [test[target - nums[i]], i]
            else:
                test[nums[i]] = i
        

        