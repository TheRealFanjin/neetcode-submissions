from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l,r = 0, len(self.store[key]) - 1
        res = ""
        while l <= r:
            mid = l + (r - l) // 2
            if self.store[key][mid][0] <= timestamp:
                res = self.store[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res