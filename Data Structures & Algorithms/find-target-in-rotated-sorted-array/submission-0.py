class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2:
            mid = nums[p1 + ((p2 - p1) // 2)]
            print(mid)
            if mid == target:
                return p1 + ((p2 - p1) // 2)
            elif nums[p1] == target:
                return p1
            elif nums[p2] == target:
                return p2
            if mid > nums[p1] and nums[p1] < target < mid:
                p2 = p1 + ((p2 - p1) // 2) - 1
            elif mid > nums[p1] or (mid < nums[p2] and mid < target < nums[p2]):
                p1 = p1 + ((p2 - p1) // 2) + 1
            else:
                p2 = p1 + ((p2 - p1) // 2) - 1
        return -1

        