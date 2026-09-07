class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -1
        l,r = 0, len(heights) - 1
        while l < r:
            amount = (r - l) * min(heights[l], heights[r])
            if amount > res:
                res = amount
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res