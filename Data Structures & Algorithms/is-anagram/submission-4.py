class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in s:
            if i in sdict:
                sdict[i] += 1
            else:
                sdict[i] = 1
        for j in t:
            if j in tdict:
                tdict[j] += 1
            else:
                tdict[j] = 1
        if len(sdict) > len(tdict):
            for k in sdict:
                if k not in tdict or tdict[k] != sdict[k]:
                    return False
            return True
        else:
            for k in tdict:
                if k not in sdict or tdict[k] != sdict[k]:
                    return False
            return True