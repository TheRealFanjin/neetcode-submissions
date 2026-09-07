class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            lower_height = min(heights[l], heights[r])
            if lower_height * (r - l) > max_area:
                max_area = lower_height * (r - l)
            if lower_height == heights[l]:
                l += 1
            else:
                r -= 1
        return max_area          