class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recur(idx, curr):
            if idx == len(nums):
                nonlocal res
                res.append(list(curr))
                return
            curr.append(nums[idx])
            recur(idx + 1, curr)
            curr.pop()
            recur(idx + 1, curr)
        recur(0, [])
        return res