class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        

    def addNum(self, num: int) -> None:

        if len(self.low) == len(self.high):
            new_num = heapq.heappushpop(self.high, num)
            heapq.heappush_max(self.low, new_num)
        else:
            new_num = heapq.heappushpop_max(self.low, num)
            heapq.heappush(self.high, new_num)
# low 1 3
# high 2
    def findMedian(self) -> float:
        if len(self.low) != len(self.high):
            return self.low[0]
        else:
            return (self.low[0] + self.high[0])/2