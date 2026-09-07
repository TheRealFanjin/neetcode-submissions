class Solution:
    def minWindow(self, s: str, t: str) -> str:
        list_t = list(t)
        l,r = 0,0
        min_substring = ""
        t_dict = {}
        for i in t:
            if i not in t_dict:
                t_dict[i] = 0
            t_dict[i] += 1
        t_dict_copy = t_dict.copy()
        while r != len(s):
            print('l', s[l])
            print('r', s[r])
            if s[r] in t_dict_copy:
                t_dict_copy[s[r]] -= 1
                if t_dict_copy[s[r]] == 0:
                    del t_dict_copy[s[r]]
                if not t_dict_copy:
                    if not min_substring or len(min_substring) > r - l + 1:
                        min_substring = s[l:r + 1]
                    t_dict_copy = t_dict.copy()
                    l += 1
                    r = l - 1
            r += 1
        return min_substring
            
        