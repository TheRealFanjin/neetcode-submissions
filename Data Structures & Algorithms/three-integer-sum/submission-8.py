from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        duplicates = set()
        for i in range(len(nums)):
            j,k = i + 1, len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    if (nums[i], nums[j], nums[k]) not in duplicates:
                        res.append([nums[i], nums[j], nums[k]])
                        duplicates.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return res
        