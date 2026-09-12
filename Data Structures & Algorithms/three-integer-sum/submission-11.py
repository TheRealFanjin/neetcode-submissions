class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        dup = set()
        for i in range(len(nums)):
            l,r = i + 1, len(nums) - 1
            target = nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if -total == target and (target, nums[l], nums[r]) not in dup:
                    res.append([target, nums[l], nums[r]])
                    dup.add((target, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif -total > target:
                    l += 1
                else:
                    r -= 1
        return res