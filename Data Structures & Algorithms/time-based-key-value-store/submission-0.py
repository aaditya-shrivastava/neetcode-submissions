class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        ans = ""
        for time, value in self.store[key]:
            if time <= timestamp:
                ans = value
            else:
                break
        return ans