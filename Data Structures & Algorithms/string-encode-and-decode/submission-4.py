class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        res = str(len(strs[0])) + '#' + strs[0] 
        for s in strs[1:]:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        out = []
        counter = 0
        while counter < len(s):
            num = ''
            while s[counter] != '#':
                num += s[counter]
                counter += 1
            num = int(num)
            out.append(s[counter + 1:counter + num + 1])
            counter += num + 1
        return out