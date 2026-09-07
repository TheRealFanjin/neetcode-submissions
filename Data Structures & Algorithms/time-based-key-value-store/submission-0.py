class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d or self.d[key][0][0] > timestamp:
            return ""
        if self.d[key][-1][0] <= timestamp:
            return self.d[key][-1][1]
        i = 0
        j = len(self.d[key]) - 1
        while i < j:
            mid = i + (j - i) // 2
            if self.d[key][mid][0] == timestamp:
                return self.d[key][mid][1]
            elif self.d[key][mid][0] > timestamp:
                j = mid - 1
            elif self.d[key][mid][0] < timestamp:
                i = mid + 1
        if self.d[key][i][0] <= timestamp:
            return self.d[key][i][1]
        else:
            return self.d[key][i - 1][1]
        
