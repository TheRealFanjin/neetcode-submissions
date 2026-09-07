class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        window = set()
        res = 0
        while r != len(s):
            if r - l > res:
                res = r - l
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            r += 1
        if r - l > res:
                res = r - l
        return res