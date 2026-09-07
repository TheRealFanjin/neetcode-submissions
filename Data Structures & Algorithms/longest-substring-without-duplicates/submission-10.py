class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l,r = 0,0
        window_set = set()
        longest = 0
        while True:
            if s[r] in window_set:
                while s[l] != s[r]:
                    window_set.remove(s[l])
                    l += 1
                window_set.remove(s[l])
                l += 1
            if r - l + 1 > longest:
                longest = r - l + 1
            if r == len(s) - 1:
                break
            window_set.add(s[r])
            r += 1
        return longest