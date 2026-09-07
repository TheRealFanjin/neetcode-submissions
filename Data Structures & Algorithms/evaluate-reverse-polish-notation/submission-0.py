class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem == '+':
                a = stack[-1]
                del stack[-1]
                b = stack[-1]
                del stack[-1]
                stack.append(a + b)
            elif elem == '-':
                a = stack[-1]
                del stack[-1]
                b = stack[-1]
                del stack[-1]
                stack.append(b - a)
            elif elem == '*':
                a = stack[-1]
                del stack[-1]
                b = stack[-1]
                del stack[-1]
                stack.append(a * b)
            elif elem == '/':
                a = stack[-1]
                del stack[-1]
                b = stack[-1]
                del stack[-1]
                ans = b / a
                if ans < 0 and ans % 1 != 0:
                    stack.append(b//a + 1)
                else:
                    stack.append(b//a)
                print(a)
                print(b)
                print(b//a)
            else:
                stack.append(int(elem))
        return stack[0]
        