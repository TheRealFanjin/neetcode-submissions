class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        ans = []
        for i, elem in enumerate(temperatures):
            while tempStack and tempStack[-1][1] < elem:
                ans[tempStack[-1][0]] = i - tempStack[-1][0]
                del tempStack[-1]
            if i == len(temperatures) - 1:
                ans.append(0)
            elif temperatures[i + 1] > elem:
                ans.append(1)
            else:
                tempStack.append((i, elem))
                ans.append(0)
        return ans

        