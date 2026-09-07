from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            char_freq = [0] * 26
            for c in word:
                char_freq[ord(c) - 97] += 1
            d[tuple(char_freq)].append(word)
        out = []
        for anagram in d:
            out.append(d[anagram])
        return out
        