class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputList = []
        outputDict = {}
        for num,item in enumerate(strs):
            matched = False
            itemDict = {}
            for leter in item:
                if leter in itemDict:
                    itemDict[leter] += 1
                else:
                    itemDict[leter] = 1
            for index,result in enumerate(outputList):
                if len(result[0]) != len(item):
                    continue
                
                if itemDict == outputDict[index]:
                    # if it got in
                    outputList[index].append(item)
                    matched = True
                    break
            if not matched:
                outputList.append([item])
                outputDict[len(outputDict)] = itemDict
        return outputList
        