class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_products = [1]
        r_products = [1]
        for i in range(len(nums) - 1):
            l_products.append(nums[i] * l_products[-1])
            r_products.insert(0, nums[-i - 1] * r_products[0])
        return [l_products[i] * r_products[i] for i in range(len(nums))]