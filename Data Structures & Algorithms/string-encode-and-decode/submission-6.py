class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for strr in strs:
            res += f'{len(strr)}#{strr}'
        return res
    def decode(self, s: str) -> List[str]:
        decoded = []
        idx = 0
        print(s)
        while idx < len(s):
            length = ''
            while s[idx] != '#':
                length += s[idx]
                idx += 1
            length = int(length)
            decoded.append(s[idx + 1:idx + length + 1])
            idx += length + 1
        return decoded