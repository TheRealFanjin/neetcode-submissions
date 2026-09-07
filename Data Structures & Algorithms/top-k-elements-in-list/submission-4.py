class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freq = []
        freqSet = set()
        for element in nums:
            if element in dic:
                dic[element] += 1
            else:
                dic[element] = 1

            if element not in freqSet:
                if len(freq) != k:
                    freq.append(element)
                    freqSet.add(element)
                else:
                    for count,elem in enumerate(freq):
                        if dic[element] > dic[elem]:
                            freq[count] = element
                            freqSet.remove(elem)
                            freqSet.add(element)
                            break
            print(freq)

        return freq
                