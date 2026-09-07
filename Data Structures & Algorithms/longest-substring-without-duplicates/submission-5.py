class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        s = [char for char in s]
        l,r = 0,1

        longest = 0

        while r < len(s):
            print('l', l)
            print('r', r)
            if s[r] in s[l: r]:
                if r - l > longest:
                    longest = r - l
                l += 1
            else:
                r += 1
                if r >= len(s) and r - l > longest:
                    longest = r - l

        return longest
        