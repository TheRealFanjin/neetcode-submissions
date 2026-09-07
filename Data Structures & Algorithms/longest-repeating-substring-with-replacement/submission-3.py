class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        freq = defaultdict(int)
        freq[s[l]] += 1
        max_freq = 1
        res = 1
        while r != len(s) - 1:
            r += 1
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])
            if r - l - max_freq + 1 > k:
                freq[s[l]] -= 1
                l += 1
                continue
            if r - l + 1 > res:
                res = r - l + 1
        return res
