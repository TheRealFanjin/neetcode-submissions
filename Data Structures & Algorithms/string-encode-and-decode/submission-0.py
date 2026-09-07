class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for word in strs:
            result += word + '!..!'
        return result

    def decode(self, s: str) -> List[str]:
        result = s.split('!..!')
        del result[len(result) - 1]
        word = ''
        """for count in range(len(s)):
            if s[count] == '!' and s[count + 1] == '.' and s[count + 2] == '.' and s[count + 3] == '!':
                print(result)
                print(s)
                word = s[:count]
                result.append(word)
                s = s[4:]
                print('after', s)
                count += 4
                if len(s) == 0:
                    break"""
        return result
