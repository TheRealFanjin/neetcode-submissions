class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for val in tokens:
            if val.isdigit() or (val.startswith('-') and len(val) > 1):
                s.append(int(val))
            else:
                if val == "+":
                    s.append(s.pop() + s.pop())
                elif val == "-":
                    last = s.pop()
                    s.append(s.pop() - last)
                elif val == "*":
                    s.append(s.pop() * s.pop())
                else:
                    last = s.pop()
                    s.append(int(s.pop() / last))
        return s[0]