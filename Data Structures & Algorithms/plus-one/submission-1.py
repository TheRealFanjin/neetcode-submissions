class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        carry = True
        for i in range(len(digits) - 1,  -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            elif carry:
                digits[i] += 1
                carry = False
                break
        if carry:
            return [1] + digits
        return digits