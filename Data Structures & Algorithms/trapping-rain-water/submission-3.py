class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)
        total = 0
        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], height[i + 1])
        for i in range(len(height)):
            if min(prefix_max[i], suffix_max[i]) > height[i]:
                total += min(prefix_max[i], suffix_max[i]) - height[i]
        return total