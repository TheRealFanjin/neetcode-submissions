class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_letters = [0] * 26
        s2_letters = [0] * 26
        for i in range(len(s1)):
            s1_letters[ord(s1[i]) - 97] += 1
            s2_letters[ord(s2[i]) - 97] += 1
        for l in range(len(s2) - len(s1)):
            print(l, s1_letters, s2_letters, sep='\n')
            if s1_letters == s2_letters:
                return True
            s2_letters[ord(s2[l + len(s1)]) - 97] += 1
            s2_letters[ord(s2[l]) - 97] -= 1
        if s1_letters == s2_letters:
            return True
        return False