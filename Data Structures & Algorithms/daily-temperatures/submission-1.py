class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for idx,temp in enumerate(temperatures):
            if not stack:
                stack.append(idx)
                continue
            while stack and temp > temperatures[stack[-1]]:
                res[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)
        return res