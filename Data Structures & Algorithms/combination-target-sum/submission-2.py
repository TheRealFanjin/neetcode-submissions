class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx, curr, curr_sum):
            if curr_sum == target:
                nonlocal res
                res.append(list(curr))
                return
            if idx == len(nums) or curr_sum > target:
                return
            curr.append(nums[idx])
            backtrack(idx, curr, curr_sum + nums[idx])
            curr.pop()
            backtrack(idx + 1, curr, curr_sum)
        backtrack(0, [], 0)
        return res