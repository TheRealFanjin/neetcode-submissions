class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        if s == s[::-1]:
            return True
        return False