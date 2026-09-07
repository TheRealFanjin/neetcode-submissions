from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            char_list = [0] * 26
            for letter in word:
                char_list[ord(letter) - 97] += 1
            d[tuple(char_list)].append(word)
        res = [anagram for anagram in d.values()]
        return res
