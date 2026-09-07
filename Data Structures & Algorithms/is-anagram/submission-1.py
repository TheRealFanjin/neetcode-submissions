class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        set_s = {}
        set_t = {}

        for char in s:
            if char not in set_s.keys():
                set_s[char] = 0
            set_s[char] += 1
        
        for char in t:
            if char not in set_t.keys():
                set_t[char] = 0
            set_t[char] += 1
        
        for key, value in set_s.items():
            if key not in set_t.keys():
                return False
            if set_t[key] != value:
                return False
        
        return True