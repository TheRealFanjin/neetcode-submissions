class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[mid] == target:
                return mid
            
            if nums[l] < nums[mid]:
                if nums[l] < target < nums[mid]:
                    r = mid - 1
                    l += 1
                else:
                    l = mid + 1
                    r -= 1
            else:
                if nums[mid] < target < nums[r]:
                    l = mid + 1
                    r -= 1
                else:
                    r = mid - 1
                    l += 1
        return -1