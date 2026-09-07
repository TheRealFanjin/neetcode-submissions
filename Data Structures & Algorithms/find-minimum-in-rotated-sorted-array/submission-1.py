class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        minimum = nums[0]
        while l < r:
            mid = l + (r - l) // 2
            if nums[l] < nums[r]:
                return min(nums[l], minimum)
            print(l,r)
            minimum = min(nums[l], nums[r], nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid - 1
        return minimum