class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        setted = set(nums)
        dupsi = []
        dupse = []
        output = []
        for i in range(0, len(nums)):
            first = nums[i]
            for j in range(i + 1, len(nums)):
                second = nums[j]
                if -first - second in setted and nums.index(-first-second) != i and nums.index(-first-second) != j and {i, j, nums.index(-first-second)} not in dupsi and {first, second, -first-second} not in dupse:
                    output.append([first, second, -first-second])
                    dupsi.append({i, j, nums.index(-first-second)})
                    dupse.append({first, second, -first-second})
        return output