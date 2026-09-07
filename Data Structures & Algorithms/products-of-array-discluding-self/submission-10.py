class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        totalNo0 = 1
        zerocount = 0
        result = []
        for i in nums:
            total *= i
            if i != 0:
                totalNo0 *= i
            elif i == 0:
                zerocount += 1

        
        for j in nums:
            if zerocount > 1:
                result.append(0)
            elif j == 0:
                result.append(round(totalNo0))
            else:
                result.append(round(total/j))
        return result
        