class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point1 = 0
        point2 = len(numbers) - 1

        while True:
            total = numbers[point1] + numbers[point2]
            if total == target:
                return [point1 + 1, point2 + 1]
            elif total < target:
                point1 += 1
            elif total > target:
                point2 -= 1