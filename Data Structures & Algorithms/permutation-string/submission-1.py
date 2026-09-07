class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l,r = 0,0
        letters1 = {}
        for i in s1:
            if i not in letters1:
                letters1[i] = 0
            letters1[i] += 1
        checking = False
        letters = letters1.copy()
        while r != len(s2):
            current_elem = s2[r]
            print(current_elem)

            if current_elem in letters and letters[current_elem] != 0:
                if not checking:
                    l = r
                    checking = True

                letters[current_elem] -= 1
                summ = 0
                for i in letters:
                    summ += letters[i]
                if summ == 0:
                    return True
            else:
                if checking:
                    letters = letters1.copy()
                    checking = False
                    l += 1
                    r = l - 1

            r += 1
        return False