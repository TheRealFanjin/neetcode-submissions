class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [['(', 1, 0]]
        output = []
        while stack:
            curr = stack[-1]
            del stack[-1]
            if curr[1] == n and curr[2] == n:
                output.append(curr[0])
                continue
            if curr[1] < n:
                first = curr.copy()
                first[0] += '('
                first[1] += 1
                stack.append(first)
            if curr[2] < n and curr[2] < curr[1]:
                second = curr.copy()
                second[0] += ')'
                second[2] += 1
                stack.append(second)
        return output