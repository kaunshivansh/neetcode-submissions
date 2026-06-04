from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        heappush(self.small, -num)

        heappush(self.large, -heappop(self.small))

        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2.0