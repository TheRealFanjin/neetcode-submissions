class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        if nums1 and nums2:
            while p1 + p2 < ((len(nums1) + len(nums2) - 1) // 2):
                if nums1[p1] > nums2[p2]:
                    p2 += 1
                else:
                    p1 += 1
        
            if (len(nums1) + len(nums2)) % 2 == 0:
                return (nums1[p1] + nums2[p2]) / 2
            else:
                if nums2[p2] > nums1[p1]:
                    return nums1[p1]
                else:
                    return nums2[p2]
        else:
            nums = None
            if nums1:
                nums = nums1
            else:
                nums = nums2
            mid = len(nums) // 2
            if len(nums) % 2 == 0:
                return (nums[mid] + nums[mid - 1]) / 2
            else:
                return nums[mid]
