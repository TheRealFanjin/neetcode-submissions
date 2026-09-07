class Solution:
    def isValid(self, s: str) -> bool:
        queue = []
        for char in s:
            if char in '({[':
                queue.append(char)
            else:
                print(queue)
                if len(queue) == 0 or char == ']' and queue[len(queue) - 1] != '[' or char == '}' and queue[len(queue) - 1] != '{' or char == ')' and queue[len(queue) - 1] != '(':
                    return False
                else:
                    del queue[len(queue) - 1]
        if len(queue) == 0:
            return True
        else:
            return False