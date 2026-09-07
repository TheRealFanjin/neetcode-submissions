class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6] - [1, 1, 2, 8] - [48, 24, 6, 1]
        prefix = [1]
        suffix = [1]
        out = []
        for i in range(0, len(nums) - 1):
            prefix.append(prefix[-1] * nums[i])
            suffix.insert(0, suffix[0] * nums[len(nums) - i - 1])
        for i in range(len(nums)):
            out.append(prefix[i] * suffix[i])
        return out

        