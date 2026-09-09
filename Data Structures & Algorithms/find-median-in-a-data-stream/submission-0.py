class MedianFinder:

    def __init__(self):
        self.medianFinder = []

    def addNum(self, num: int) -> None:
        self.medianFinder.append(num)
        


    def findMedian(self) -> float:
        self.medianFinder.sort()
        n = len(self.medianFinder)
        if n%2 == 1:
            return self.medianFinder[(n//2)]
        else: 
            return (self.medianFinder[n//2] + self.medianFinder[(n//2)-1]) / 2.0        