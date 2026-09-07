class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)
        for strr in strs:
            char_count = [0] * 26
            for char in strr:
                char_count[ord(char) - 97] += 1
            res_dict[tuple(char_count)].append(strr)
        res = []
        for val in res_dict.values():
            res.append(val)
        return res
