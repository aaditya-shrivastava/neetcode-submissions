class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)
        self.data.sort()

    def findMedian(self) -> float:
        n= len(self.data)
        if n % 2 == 1:
            return float(self.data[n//2])
        else:
            mid1 = self.data[n//2 -1]
            mid2 = self.data[n//2]
            return (float(mid1)+ float(mid2)) / 2.0 