class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dedup = set()
        res = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if total == -nums[i] and (nums[i], nums[l], nums[r]) not in dedup:
                    res.append([nums[i],nums[l],nums[r]])
                    dedup.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total > -nums[i]:
                    r -= 1
                else:
                    l += 1
        return res
