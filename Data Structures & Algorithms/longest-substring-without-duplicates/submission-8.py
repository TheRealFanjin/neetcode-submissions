class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1 = 0
        p2 = 0
        string_set = set()
        longest_substring = 1
        if s:
            string_set.add(s[p1])
        else:
            return 0

        while p2 != len(s) - 1 and s:
            print(string_set, p1, p2)
            p2 += 1
            if s[p2] in string_set:
                while s[p1] != s[p2]:
                    string_set.remove(s[p1])
                    p1 += 1
                p1 += 1
            string_set.add(s[p2])

            if p2 - p1 + 1 > longest_substring:
                longest_substring = p2 - p1 + 1

        return longest_substring
            