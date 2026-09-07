class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        minimum = nums[0]
        while i <= j:
            mid = i + (j - i) // 2
            if nums[mid] < minimum:
                minimum = nums[mid]

            if nums[i] < minimum:
                minimum = nums[i]

            if nums[j] < minimum:
                minimum = nums[j]

            if nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[i]:
                j = mid - 1
            else:
                break
        return minimum
        