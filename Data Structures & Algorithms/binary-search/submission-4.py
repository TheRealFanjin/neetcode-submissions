class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while True:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            if mid == l:
                return -1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1