class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol, psum = [], [], []

        def backtrack(i):
            if i == len(nums) or psum and psum[-1] > target: return

            if psum and psum[-1] == target:
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            psum.append(psum[-1] + nums[i]) if psum else psum.append(nums[i])

            backtrack(i)

            del sol[-1]
            del psum[-1]

            backtrack(i + 1)
        
        backtrack(0)
        return res